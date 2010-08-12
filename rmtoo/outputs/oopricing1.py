#
#  -*- coding: utf-8 -*-
#
# OpenOffice Pricing output class for rmtoo
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.TopologicalSort import topological_sort

# imports from python-odf
from odf.opendocument import OpenDocumentSpreadsheet
import odf.table
import odf.text
import odf.style
import odf.office
import odf.form
import odf.draw
import odf.number

class oopricing1:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]
        self.doc_styles = {}
        
        self.setup_coord_lookup()

    def setup_coord_lookup(self):
        alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
        pairs = [''.join((x,y)) for x in alpha for y in [''] + [z for z in alpha]]
        self.sscoords=sorted(pairs, key=len)

    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)
  
    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        #  XXX ToDo
        assert(False)
        
    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continnum_latest())

    def output_reqset(self, reqset):
        # Everything here needs a stable order - also a topological
        # order makes sense.
        sreqs = topological_sort(reqset)

        # Because of a problem with the current OpenOffice versions,
        # there is the need to sometimes arrange requirements as rows
        # and sometimes as columns.
        # The order dictionary holds the number - which can be
        # computed in a row or column.
        # XXX NEEDED????
        ##order = {}

        ##cnt = 0
        ##for req in sreqs:
        ##    order[req] = cnt
        ##    cnt += 1

        calcdoc = OpenDocumentSpreadsheet()
        self.create_styles(calcdoc)
        self.create_costs_sheet(calcdoc, sreqs)
        self.create_deps_sheet(calcdoc, sreqs)
        self.create_sums_sheet(calcdoc, sreqs)
        self.create_constants_sheet(calcdoc)
        calcdoc.save(self.output_filename, True)

    # There is the need to apply some styles
    def create_styles(self, calcdoc):
        # Bold
        tc_font_bold = odf.style.Style(name="tc-bold", family="table-cell")
        tc_font_bold.addElement(
            odf.style.TextProperties(fontweight="bold", fontsize="12pt"))
        calcdoc.automaticstyles.addElement(tc_font_bold)
        self.doc_styles["tc-bold"] = tc_font_bold

        # Bold with blue background for header
        tc_bold_blue = odf.style.Style(name="tc-bold-blue", family="table-cell")
        tc_bold_blue.addElement(
            odf.style.TextProperties(fontweight="bold", fontsize="12pt"))
        tc_bold_blue.addElement(
            odf.style.TableCellProperties(backgroundcolor="#99ccff"))
        calcdoc.automaticstyles.addElement(tc_bold_blue)
        self.doc_styles["tc-bold-blue"] = tc_bold_blue

        # Column Style: 1,2'' wide
        tabcol12 = odf.style.Style(name="col-ids", family="table-column")
        tabcol12.addElement(
            odf.style.TableColumnProperties(columnwidth="1.2in"))
        calcdoc.automaticstyles.addElement(tabcol12)
        self.doc_styles["col-ids"] = tabcol12

        # Column Style for name: 2.25'' wide
        tcs = odf.style.Style(name="col-name", family="table-column")
        tcs.addElement(
            odf.style.TableColumnProperties(columnwidth="2.25in"))
        calcdoc.automaticstyles.addElement(tcs)
        self.doc_styles["col-name"] = tcs

        # Column Style for compliant: 0.75'' wide
        tcs = odf.style.Style(name="col-compliant", family="table-column")
        tcs.addElement(
            odf.style.TableColumnProperties(columnwidth="0.75in"))
        calcdoc.automaticstyles.addElement(tcs)
        self.doc_styles["col-compliant"] = tcs

        # Column Style for Euro: only full Euros.
        # The positive part
        tcs = odf.number.CurrencyStyle(name="cs-euro-positive",
                                       volatile="true")
        tcs.addElement(odf.number.Number(
                decimalplaces="0", grouping="true", minintegerdigits="1"))
        tcs.addElement(odf.number.Text(text=" "))
        tcs.addElement(odf.number.CurrencySymbol(
                text=u"€", country="DE", language="de"))
        calcdoc.styles.addElement(tcs)

        # This is the negaive part: there is the decision, which one
        # is used.
        tcs = odf.number.CurrencyStyle(name="cs-euro")
        tcs.addElement(odf.number.Text(text="-"))
        tcs.addElement(odf.number.Number(
                decimalplaces="0", grouping="true", minintegerdigits="1"))
        tcs.addElement(odf.number.Text(text=" "))
        tcs.addElement(odf.number.CurrencySymbol(
                text=u"€", country="DE", language="de"))
        tcs.addElement(odf.style.Map(
                applystylename="cs-euro-positive", condition="value()>=0"))
        calcdoc.styles.addElement(tcs)

        tcs = odf.style.Style(name="col-euro", family="table-cell",
                              datastylename="cs-euro")
        calcdoc.automaticstyles.addElement(tcs)
        self.doc_styles["col-euro"] = tcs

    def create_costs_sheet(self, calcdoc, sreqs):
        sheet = odf.table.Table(name="Costs")
        self.create_form(sheet, sreqs)
        self.create_costs_column_styles(sheet)
        self.create_costs_header(sheet)
        self.create_costs_content(sheet, sreqs)
        calcdoc.spreadsheet.addElement(sheet)

    def create_deps_sheet(self, calcdoc, sreqs):
        sheet = odf.table.Table(name="Deps")
        self.create_deps_names(sheet, sreqs)
        # The second row is where all the results will be inserted.
        # Therefore put in each one a none.
        tr = odf.table.TableRow()
        for _ in sreqs:
            self.create_text_cell(tr, "none")
        sheet.addElement(tr)
        # The third row contains the indices of the requirement
        # which is chosen as the dependent one.
        tr = odf.table.TableRow()
        for _ in sreqs:
            tc = odf.table.TableCell(value="1", valuetype="float")
            p = odf.text.P(text="1")
            tc.addElement(p)
            tr.addElement(tc)
        sheet.addElement(tr)

        self.create_empty_row(sheet)
        # Output all the dependent requirements
        self.create_deps_dependent(sheet, sreqs)
        calcdoc.spreadsheet.addElement(sheet)

    def create_sums_sheet(self, calcdoc, sreqs):
        sheet = odf.table.Table(name="Sums")
        calcdoc.spreadsheet.addElement(sheet)

    def create_constants_sheet(self, calcdoc):
        sheet = odf.table.Table(name="Constants")
        # This is the list where the requirement compliance gets it
        # values from. 
        for r in ["none", "partial", "fully"]:
            tr = odf.table.TableRow()
            tc = odf.table.TableCell()
            p = odf.text.P(text=r)
            tc.addElement(p)
            tr.addElement(tc)
            sheet.addElement(tr)
        calcdoc.spreadsheet.addElement(sheet)

    ### 2nd level functions

    # Create an empty row
    @staticmethod
    def create_empty_row(sheet):
        tr = odf.table.TableRow()
        sheet.addElement(tr)

    @staticmethod
    def create_empty_cell(row):
        tc = odf.table.TableCell()
        row.addElement(tc)
    
    # Create the first row in the deps sheet: all the names
    def create_deps_names(self, sheet, sreqs):
        tr = odf.table.TableRow()
        for req in sreqs:
            tc = odf.table.TableCell()
            p = odf.text.P(text=req.name)
            tc.addElement(p)
            tr.addElement(tc)
        sheet.addElement(tr)

    def create_deps_dependent(self, sheet, sreqs):
        # The number of the following rows depend on the maximum
        # number of outgoing requirements.
        # This flags if there is something found with the current
        # index.
        i=0
        while True:
            tr = odf.table.TableRow()
            index_used=False
            for req in sreqs:
                if len(req.outgoing)>i:
                    tc = odf.table.TableCell()
                    p = odf.text.P(text=req.outgoing[i].name)
                    tc.addElement(p)
                    tr.addElement(tc)
                    index_used=True
                else:
                    tc = odf.table.TableCell()
                    tr.addElement(tc)
            sheet.addElement(tr)
            if not index_used:
                break
            i+=1

    def create_costs_column_styles(self, sheet):
        # Colum: Ids
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-ids"])
        sheet.addElement(tc)
        # Colum: Name
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-name"])
        sheet.addElement(tc)
        # Colum: Compliant
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-compliant"])
        sheet.addElement(tc)
        # Colum: Costs-dayrate
        tc = odf.table.TableColumn(
            stylename=self.doc_styles["col-ids"],
            defaultcellstylename=self.doc_styles["col-euro"])
        sheet.addElement(tc)
        # Colum: Costs-days
        tc = odf.table.TableColumn()
        sheet.addElement(tc)
        # Colum: Costs-material
        tc = odf.table.TableColumn()
        sheet.addElement(tc)
        # Colum: Costs-sum
        tc = odf.table.TableColumn()
        sheet.addElement(tc)
        # Colum: Dependent from
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-ids"])
        sheet.addElement(tc)
       
    @staticmethod
    def create_text_cell(table_row, text, style=None):
        if style!=None:
            tc = odf.table.TableCell(stylename=style)
        else:
            tc = odf.table.TableCell()

        if text!=None:
            p = odf.text.P(text=text)
            tc.addElement(p)
        table_row.addElement(tc)

    def create_costs_header(self, sheet):
        # First is empty
        self.create_empty_row(sheet)
        # Second holds only the Overall sum
        tr = odf.table.TableRow()
        self.create_text_cell(tr, "",
                              self.doc_styles["tc-bold"])
        sheet.addElement(tr)
        # Followed by an additionally empty line
        self.create_empty_row(sheet)
        # Table header line 1
        tr = odf.table.TableRow()
        for h in ["Id", "Name", "Compliant", "Costs for requirement",
                  None, None, None, "Dependent from", 
                  "Costs of dependent", None, None,
                  "Overall sum", None, None, "Comment"]:
            self.create_text_cell(tr, h, self.doc_styles["tc-bold-blue"])
        sheet.addElement(tr)
        # Table header line 2
        tr = odf.table.TableRow()
        for h in [None, None, None, "dayrate",
                  "#days", "material", "sum", None, 
                  "rate", "material", "sum",
                  "rate", "material", "sum", None]:
            self.create_text_cell(tr, h, self.doc_styles["tc-bold-blue"])
        sheet.addElement(tr)

    def create_costs_content(self, sheet, sreqs):
        i=6
        for req in sreqs:
            tr = odf.table.TableRow()
            self.create_costs_content_req(tr, req, i)
            sheet.addElement(tr)
            i+=1

    def create_costs_content_req(self, tr, req, i):
        # First cell is the id
        self.create_text_cell(tr, req.name)
        # Second cell is the name
        self.create_text_cell(tr, req.tags["Name"])
        # Third is the compliant
        tc = odf.table.TableCell()
        dc = odf.draw.Control(control="lbcompliant%s" % req.name,
                              zindex="0",
                              x="0.0in",
                              y="0.0in",
                              endcelladdress="Costs.C%d" % (i+1),
                              endx="0.75in",
                              endy="0.0in")
        tc.addElement(dc)
        tr.addElement(tc)
        # Three empty columns for costs
        self.create_empty_cell(tr)
        self.create_empty_cell(tr)
        self.create_empty_cell(tr)
        # Sum / factor of before ones
        tc = odf.table.TableCell(
            valuetype="currency", formula="oooc:=[.D%d]*[.E%d]+[.F%d]" % (i, i, i))
        tr.addElement(tc)
        # Dependent on Chooser
        tc = odf.table.TableCell()
        # Do not do this for first cell.
        if len(req.outgoing)>0:
            dc = odf.draw.Control(control="lbdependentfrom%s" % req.name,
                                  zindex="0",
                                  x="0.0in",
                                  y="0.0in",
                                  endcelladdress="Costs.H%d" % (i+1),
                                  endx="1.2in",
                                  endy="0.0in")
            tc.addElement(dc)
        tr.addElement(tc)

    def create_form(self, calcdoc, sreqs):
        forms = odf.office.Forms(
            applydesignmode="false",
            automaticfocus="false"
            )
        form = odf.form.Form(
            applyfilter="true",
            commandtype="table",
            controlimplementation="ooo:com.sun.star.form.component.Form",
            name="Standard",
            targetframe="",
            href="")

        # Listboxes for compliant
        i=0
        for req in sreqs:
            lb = odf.form.Listbox(
                id="lbcompliant%s" % req.name,
                boundcolumn="1",
                dropdown="yes",
                controlimplementation="ooo:com.sun.star.form.component.ListBox",
                linkedcell="Deps.%s2" % self.sscoords[i],
                listlinkagetype="selection",
                name="ListBox Compliant %s" % req.name,
                size="3",
                sourcecellrange="Constants.A1:Constants.A3"
                )
            lbproperties = odf.form.Properties()
            lbprop = odf.form.Property(
                propertyname="DefaultControl",
                stringvalue="com.sun.star.form.control.ListBox",
                valuetype="string")
            lbproperties.addElement(lbprop)
            # Default selection
            lstprop = odf.form.ListProperty(
                propertyname="DefaultSelection",
                valuetype="float")
            defaultval = odf.form.ListValue(stringvalue='value="0"')
            lstprop.addElement(defaultval)
            lbproperties.addElement(lstprop)

            lb.addElement(lbproperties)

            form.addElement(lb)
            i+=1

        # Listboxes for dependent from
        i=0
        for req in sreqs:
            # When there is only one entry in the list, there is no
            # need to have a dropdown list.
            ddown="yes"
            if len(req.outgoing)<=1:
                ddown="no"

            lb = odf.form.Listbox(
                id="lbdependentfrom%s" % req.name,
                boundcolumn="1",
                dropdown="yes",
                controlimplementation="ooo:com.sun.star.form.component.ListBox",
                linkedcell="Deps.%s3" % self.sscoords[i],
                listlinkagetype="selection-indexes",
                name="ListBox Dependet From %s" % req.name,
                size="3",
                sourcecellrange="Deps.%s5:Deps.%s%d" % (
                    self.sscoords[i], self.sscoords[i], len(req.outgoing)+4)
                )
            lbproperties = odf.form.Properties()
            lbprop = odf.form.Property(
                propertyname="DefaultControl",
                stringvalue="com.sun.star.form.control.ListBox",
                valuetype="string")
            lbproperties.addElement(lbprop)
            # Default selection
            lstprop = odf.form.ListProperty(
                propertyname="DefaultSelection",
                valuetype="float")
            defaultval = odf.form.ListValue(stringvalue='value="0"')
            lstprop.addElement(defaultval)
            lbproperties.addElement(lstprop)
            # Read only
            # When there is only one dependent requirement, it makes
            # no sense to have something which can be changed.
            # Therefore this should be readonly then.
            if len(req.outgoing)<=1:
                lstprop = odf.form.Property(
                    propertyname="ReadOnly",
                    valuetype="boolean",
                    booleanvalue="true")
                lbproperties.addElement(lstprop)

            lb.addElement(lbproperties)

            form.addElement(lb)
            i+=1

        forms.addElement(form)
        calcdoc.addElement(forms)


####### OLD #######

    def formdef(self, sreqs):
        i=0
        for req in sreqs:
            print("""<form:listbox form:bound-column="1" 
form:control-implementation="ooo:com.sun.star.form.component.ListBox"
form:dropdown="true" form:id="control%d" form:linked-cell="Deps.E%d"
form:list-linkage-type="selection" form:name="ListBox"
form:size="3" form:source-cell-range="Constants.A1:Constants.A3">
<form:properties>
  <form:property form:property-name="DefaultControl"
     office:string-value="com.sun.star.form.control.ListBox"
     office:value-type="string"/>
    <form:list-property form:property-name="DefaultSelection"
        office:value-type="float">
      <form:list-value office:value="2"/>
    </form:list-property>
  </form:properties>
</form:listbox>""" % (i, i))
            i+=1


    def sheet1(self, sreqs):
        i=0
        for req in sreqs:
            # Each req is a separate row
            print('<table:table-row table:style-name="ro1">')
            # Print out id and name
            # (Note that this is no reference but a copy
            print('<table:table-cell office:value-type="string">\n'
                  '<text:p>%s</text:p>\n'
                  '</table:table-cell>' % req.name)
            print('<table:table-cell office:value-type="string">\n'
                  '<text:p>%s</text:p>\n'
                  '</table:table-cell>' % req.tags["Name"])
            # Listbox
            print('<table:table-cell>'
                  '<draw:control draw:control="control%d"'
                  'draw:text-style-name="P1" draw:z-index="1"'
                  'svg:height="0.2083in" svg:width="1.235in" svg:x="0.052in"'
                  'svg:y="0.0016in" table:end-cell-address="Costs.H%d"'
                  'table:end-x="1.287in" table:end-y="0.0244in"/>'
                  '</table:table-cell>' % (i, i))
            print('</table:table-row>')
            i+=1

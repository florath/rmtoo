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

DEPS_HEADER_LEN = 6

class oopricing1:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]
        self.doc_styles = {}
        
        self.setup_coord_lookup()

    # Because at some points a requirement will be rendered in a row
    # and at some other points as a column, there is the need to
    # access the used cell addresses from integers.
    # This function creates a map to easily acces the column name by
    # the column index: 0->A, 1->B, ..., 26->Z, 27->AA, ...
    # Note: This currently limits the number of requirements which can
    # be handled with this output module to about 700. If there is a
    # need for more requirements, this can be easily extended.
    def setup_coord_lookup(self):
        alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
        pairs = [''.join((x,y)) for x in alpha \
                     for y in [''] + [z for z in alpha]]
        self.sscoords = sorted(pairs, key=len)

    # Standard output module function
    def set_topics(self, topics):
        self.topic_set = topics.get(self.topic_name)
  
    # Create Makefile Dependencies
    def cmad(self, reqscont, ofile):
        #  XXX ToDo
        assert(False)
        
    # Note that currently the 'reqscont' is not used in case of topics
    # based output.
    def output(self, reqscont):
        # Currently just pass this to the RequirementSet
        self.output_reqset(reqscont.continnum_latest())

    def output_reqset(self, reqset):

        # This module uses also topic based output.
        # To get only those requirements into the sorted list, call
        # the following function.
        def eleminate_unused_reqs(reqset, topic_all_reqs):
            # The result is stored here.
            sreqs = []
            # Everything here needs a stable order - also a topological
            # order makes sense.
            # (Only the full requirements set can be sorted
            # topologicaly.) 
            tsreqs = topological_sort(reqset)
            # Eliminating nodes from the topoligical sort leaves the
            # order in place.
            for req in tsreqs:
                if req in topic_all_reqs:
                    sreqs.append(req)
            return sreqs

        # Because of a problem with the current OpenOffice versions,
        # there is the need to sometimes arrange requirements as rows
        # and sometimes as columns.
        # The order dictionary holds the number - which can be
        # computed in a row or column.
        def create_reqs_index(srqes):
            sreqs_index = {}
            cnt = 0
            for req in sreqs:
                sreqs_index[req] = cnt
                cnt += 1
            return sreqs_index

        # Get the used requirements
        sreqs = eleminate_unused_reqs(reqset, self.topic_set.get_all_reqs())
        # Create the row / column index of each requirement
        self.sreqs_index = create_reqs_index(sreqs)

        # Create and save the document
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

        # Column Style: 0,65'' wide
        tabcol12 = odf.style.Style(name="col-dayrate", family="table-column")
        tabcol12.addElement(
            odf.style.TableColumnProperties(columnwidth="0.65in"))
        calcdoc.automaticstyles.addElement(tabcol12)
        self.doc_styles["col-dayrate"] = tabcol12

        # Column Style: 0,8'' wide
        tabcol12 = odf.style.Style(name="col-material", family="table-column")
        tabcol12.addElement(
            odf.style.TableColumnProperties(columnwidth="0.8in"))
        calcdoc.automaticstyles.addElement(tabcol12)
        self.doc_styles["col-material"] = tabcol12

        # Column Style: 0,5'' wide
        tabcol12 = odf.style.Style(name="col-days", family="table-column")
        tabcol12.addElement(
            odf.style.TableColumnProperties(columnwidth="0.5in"))
        calcdoc.automaticstyles.addElement(tabcol12)
        self.doc_styles["col-days"] = tabcol12

        # Column Style: 0,9'' wide
        tabcol12 = odf.style.Style(name="col-sum", family="table-column")
        tabcol12.addElement(
            odf.style.TableColumnProperties(columnwidth="0.9in"))
        calcdoc.automaticstyles.addElement(tabcol12)
        self.doc_styles["col-sum"] = tabcol12

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

        # Same with read-write
        tcs = odf.style.Style(name="col-euro-rw", family="table-cell",
                              datastylename="cs-euro")
        tcs.addElement(odf.style.TableCellProperties(cellprotect="none",
                                                     printcontent="true"))
        calcdoc.automaticstyles.addElement(tcs)
        self.doc_styles["col-euro-rw"] = tcs

        # Number as used for days count
        tsc = odf.number.NumberStyle(name="ns-int")
        tsc.addElement(odf.number.Number(
                decimalplaces="0", minintegerdigits="1"))
        calcdoc.automaticstyles.addElement(tcs)

        tcs = odf.style.Style(name="col-int", family="table-cell",
                              datastylename="ns-int")
        calcdoc.automaticstyles.addElement(tcs)
        self.doc_styles["col-int"] = tcs

        # Same for rw
        tcs = odf.style.Style(name="col-int-rw", family="table-cell",
                              datastylename="ns-int")
        tcs.addElement(odf.style.TableCellProperties(cellprotect="none",
                                                     printcontent="true"))
        calcdoc.automaticstyles.addElement(tcs)
        self.doc_styles["col-int-rw"] = tcs

    def create_costs_sheet(self, calcdoc, sreqs):
        sheet = odf.table.Table(name="Costs", protected="true")
        self.create_form(sheet, sreqs)
        self.create_costs_column_styles(sheet)
        self.create_costs_header(sheet, sreqs[0])
        self.create_costs_content(sheet, sreqs)
        calcdoc.spreadsheet.addElement(sheet)

    def create_deps_sheet(self, calcdoc, sreqs):
        sheet = odf.table.Table(name="Deps") #, protected="true")
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
        for req in sreqs:
            ###tc = odf.table.TableCell(value="1", valuetype="float")
            tc = odf.table.TableCell()
            ###p = odf.text.P(text="1")
            if len(req.outgoing)>0:
                p = odf.text.P(text=req.outgoing[0].id)
                tc.addElement(p)
            tr.addElement(tc)
        sheet.addElement(tr)

        self.create_empty_row(sheet)
        # Output all the dependent requirements
        self.create_deps_dependent(sheet, sreqs)
        calcdoc.spreadsheet.addElement(sheet)

    def create_sums_sheet(self, calcdoc, sreqs):
        sheet = odf.table.Table(name="SumRate", protected="true")
        self.create_deps_names(sheet, sreqs)

        # 
        i=0
        while True:
            tr = odf.table.TableRow()
            index_used=False
            for req in sreqs:
                if len(req.incoming)>i:
                    # '[Costs.D%d]*[Costs.E%d];0)' %
                    tc = odf.table.TableCell(
                        valuetype="currency", currency="EUR",
                        formula='oooc:=IF([Deps.%s3]="%s";'
                        '[Costs.L%d];0)' %
                        (self.sscoords[self.sreqs_index[req.incoming[i]]],
                         req.name,
                         self.sreqs_index[req.incoming[i]]+DEPS_HEADER_LEN
                         ))
                    #p = odf.text.P(text=req.incoming[i].name)
                    #tc.addElement(p)
                    tr.addElement(tc)
                    index_used=True
                else:
                    tc = odf.table.TableCell()
                    tr.addElement(tc)
            sheet.addElement(tr)
            if not index_used:
                break
            i+=1

        calcdoc.spreadsheet.addElement(sheet)

        sheet = odf.table.Table(name="SumMat", protected="true")
        self.create_deps_names(sheet, sreqs)

        # 
        i=0
        while True:
            tr = odf.table.TableRow()
            index_used=False
            for req in sreqs:
                if len(req.incoming)>i:
                    tc = odf.table.TableCell(
                        valuetype="currency", currency="EUR",
                        formula='oooc:=IF([Deps.%s3]="%s";'
                        '[Costs.M%d];0)' %
                        (self.sscoords[self.sreqs_index[req.incoming[i]]],
                         req.name,
                         self.sreqs_index[req.incoming[i]]+DEPS_HEADER_LEN
                         ))
                    #p = odf.text.P(text=req.incoming[i].name)
                    #tc.addElement(p)
                    tr.addElement(tc)
                    index_used=True
                else:
                    tc = odf.table.TableCell()
                    tr.addElement(tc)
            sheet.addElement(tr)
            if not index_used:
                break
            i+=1

        calcdoc.spreadsheet.addElement(sheet)

        calcdoc.spreadsheet.addElement(sheet)

    def create_constants_sheet(self, calcdoc):
        sheet = odf.table.Table(name="Constants", protected="true")
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

    @staticmethod
    def create_empty_currency_cell(row):
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            stylename="col-euro-rw")
        tc.addElement(odf.text.P())
        row.addElement(tc)

    @staticmethod
    def create_empty_currency_cell_ro(row):
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            stylename="col-euro")
        tc.addElement(odf.text.P())
        row.addElement(tc)

    @staticmethod
    def create_empty_int_cell(row):
        tc = odf.table.TableCell(
            valuetype="float", value="0",
            stylename="col-int-rw")
        tc.addElement(odf.text.P())
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
        # 1 Colum: Ids
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-ids"])
        sheet.addElement(tc)
        # 2 Colum: Name
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-name"])
        sheet.addElement(tc)
        # 3 Colum: Compliant
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-compliant"])
        sheet.addElement(tc)
        # 4 Colum: Costs-dayrate
        tc = odf.table.TableColumn(
            stylename=self.doc_styles["col-dayrate"],
            defaultcellstylename=self.doc_styles["col-euro"])
        sheet.addElement(tc)
        # 5 Colum: Costs-days
        tc = odf.table.TableColumn(
            stylename=self.doc_styles["col-days"],
            defaultcellstylename=self.doc_styles["col-int"])
        sheet.addElement(tc)
        # 6 Colum: Costs-material
        tc = odf.table.TableColumn(
            stylename=self.doc_styles["col-material"],
            defaultcellstylename=self.doc_styles["col-euro"])
        sheet.addElement(tc)
        # 7 Colum: Costs-sum
        tc = odf.table.TableColumn(
            stylename=self.doc_styles["col-sum"],
            defaultcellstylename=self.doc_styles["col-euro"])
        sheet.addElement(tc)
        # 8 Colum: Dependent from
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-ids"])
        sheet.addElement(tc)
        # 9-14 Sum columns
        for _ in ["dep-rate", "dep-mat", "dep-sum",
                  "ovl-rate", "ovl-mat", "ovl-sum"]:
            tc = odf.table.TableColumn(
                stylename=self.doc_styles["col-sum"],
                defaultcellstylename=self.doc_styles["col-euro"])
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

    def create_costs_header(self, sheet, req):
        # First is empty
        self.create_empty_row(sheet)
        # Second holds only the Overall sum
        tr = odf.table.TableRow()
        self.create_text_cell(tr, req.id,
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
        i=0
        for req in sreqs:
            tr = odf.table.TableRow()
            self.create_costs_content_req(tr, req, i)
            sheet.addElement(tr)
            i+=1

    def create_costs_content_req(self, tr, req, i):
        choi = i + DEPS_HEADER_LEN
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
                              endcelladdress="Costs.C%d" % (choi+1),
                              endx="0.75in",
                              endy="0.0in")
        tc.addElement(dc)
        tr.addElement(tc)
        # Three empty columns for costs
        self.create_empty_currency_cell(tr)
        self.create_empty_int_cell(tr)
        self.create_empty_currency_cell(tr)
        # Sum / factor of before ones
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.D%d]*[.E%d]+[.F%d]" % (choi, choi, choi))
        tr.addElement(tc)
        # Dependent on Chooser
        tc = odf.table.TableCell()
        # Do not do this for first cell.
        if len(req.outgoing)>0:
            dc = odf.draw.Control(control="lbdependentfrom%s" % req.name,
                                  zindex="0",
                                  x="0.0in",
                                  y="0.0in",
                                  endcelladdress="Costs.H%d" % (choi+1),
                                  endx="1.2in",
                                  endy="0.0in")
            tc.addElement(dc)
        tr.addElement(tc)

        # dependet rate and material
        # Do not do this for first cell.
        if len(req.incoming)>0:
            tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=SUM([SumRate.%s2:SumRate.%s%d])" \
                % (self.sscoords[i], self.sscoords[i],
                   (1+len(req.incoming))))
            tr.addElement(tc)
        else:
            self.create_empty_currency_cell_ro(tr)

        # XXX Copy
        if len(req.incoming)>0:
            tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=SUM([SumMat.%s2:SumMat.%s%d])" \
                % (self.sscoords[i], self.sscoords[i],
                   (1+len(req.incoming))))
            tr.addElement(tc)
        else:
            self.create_empty_currency_cell_ro(tr)

        # sum of dependent
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.I%d]+[.J%d]" 
            % (i+DEPS_HEADER_LEN, i+DEPS_HEADER_LEN))
        tr.addElement(tc)

        # Overall rate
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.D%d]*[.E%d]+[.I%d]" % (i+DEPS_HEADER_LEN, i+DEPS_HEADER_LEN, i+DEPS_HEADER_LEN))
        tr.addElement(tc)
        # Overall material
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.F%d]+[.J%d]" % (i+DEPS_HEADER_LEN, i+DEPS_HEADER_LEN))
        tr.addElement(tc)
        # Overall sum
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.L%d]+[.M%d]" % (i+DEPS_HEADER_LEN, i+DEPS_HEADER_LEN))
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
                listlinkagetype="selection",
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

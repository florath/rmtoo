#  -*- coding: utf-8 -*-
'''
 rmtoo
   Free and Open Source Requirements Management Tool

  OpenOffice Pricing output class for rmtoo

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from six import iteritems

from rmtoo.lib.digraph.TopologicalSort import topological_sort
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies

# imports from python-odf
from odf.opendocument import OpenDocumentSpreadsheet
import odf.table
import odf.text
import odf.style
import odf.office
import odf.form
import odf.draw
import odf.number
import odf.dc

DEPS_HEADER_LEN = 6


class oopricing1(StdOutputParams, ExecutorTopicContinuum,
                 CreateMakeDependencies):

    def __setup_coord_lookup(self):
        '''Because at some points a requirement will be rendered in a row
           and at some other points as a column, there is the need to
           access the used cell addresses from integers.
           This function creates a map to easily acces the column name by
           the column index: 0->A, 1->B, ..., 26->Z, 27->AA, ...
           Note: This currently limits the number of requirements which can
           be handled with this output module to about 700. If there is a
           need for more requirements, this can be easily extended.'''
        alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
        pairs = [''.join((x, y)) for x in alpha
                 for y in [''] + [z for z in alpha]]
        self.__sscoords = sorted(pairs, key=len)

    def __init__(self, oconfig):
        '''Create a oopricing output object.'''
        tracer.debug("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.doc_styles = {}
        self.__used_vcs_id = None
        self.__setup_coord_lookup()

    def topic_continuum_sort(self, vcs_commit_ids, topic_sets):
        '''Because oopricing1 can only one topic continuum,
           the latest (newest) is used.'''
        self.__used_vcs_id = vcs_commit_ids[-1]
        return [topic_sets[vcs_commit_ids[-1].get_commit()]]

    def __create_meta(self):
        '''Create the meta-information for the document.'''
        m = odf.meta.Generator(text="rmtoo")
        self.__calcdoc.meta.addElement(m)
        m = odf.dc.Title(text="Requirements Pricing")
        self.__calcdoc.meta.addElement(m)
        m = odf.meta.UserDefined(name="Version",
                                 text=self.__used_vcs_id)
        self.__calcdoc.meta.addElement(m)
        m = odf.meta.UserDefined(name="Generator", text="rmtoo")
        self.__calcdoc.meta.addElement(m)

    # Functions handling style

    def __create_styles_table_cell(self):
        # Bold
        s = odf.style.Style(name="tc-bold", family="table-cell")
        s.addElement(
            odf.style.TextProperties(fontweight="bold", fontsize="12pt"))
        self.__calcdoc.automaticstyles.addElement(s)
        self.doc_styles["tc-bold"] = s

        # Bold with blue background for header
        s = odf.style.Style(name="tc-bold-blue", family="table-cell")
        s.addElement(
            odf.style.TextProperties(fontweight="bold", fontsize="12pt"))
        s.addElement(
            odf.style.TableCellProperties(backgroundcolor="#99ccff"))
        self.__calcdoc.automaticstyles.addElement(s)
        self.doc_styles["tc-bold-blue"] = s

        # Shrink-to-fit
        s = odf.style.Style(name="tc-shrink-to-fit", family="table-cell")
        s.addElement(
            odf.style.TableCellProperties(shrinktofit="true"))
        s.addElement(odf.style.TableCellProperties(cellprotect="none",
                                                   printcontent="true"))
        self.__calcdoc.automaticstyles.addElement(s)
        self.doc_styles["tc-shrink-to-fit"] = s

    def __create_styles_table_column(self):
        '''The different column style differ only in the columnwidth.'''
        colstyles = {
            "col-comment": "10in",
            "col-days": "0.5in",
            "col-dayrate": "0.65in",
            "col-compliant": "0.75in",
            "col-material": "0.8in",
            "col-sum": "0.9in",
            "col-ids": "1.2in",
            "col-name": "2.25in",
            "col-supplier": "0.75in",
            }

        # The sorted() is done to get always the same XML document -
        # which is important for comparison in tests.
        for name, size in sorted(iteritems(colstyles)):
            s = odf.style.Style(name=name, family="table-column")
            s.addElement(
                odf.style.TableColumnProperties(columnwidth=size))
            self.__calcdoc.automaticstyles.addElement(s)
            self.doc_styles[name] = s

    def __create_styles_currency(self):
        '''Column Style for Euro: only full Euros.'''
        # The positive part
        s = odf.number.CurrencyStyle(name="cs-euro-positive",
                                     volatile="true")
        s.addElement(odf.number.Number(
                decimalplaces="0", grouping="true", minintegerdigits="1"))
        s.addElement(odf.number.Text(text=" "))
        s.addElement(odf.number.CurrencySymbol(
                text=u"€", country="DE", language="de"))
        self.__calcdoc.styles.addElement(s)
        # This is the negative part: there is the decision, which one
        # is used.
        s = odf.number.CurrencyStyle(name="cs-euro")
        s.addElement(odf.number.Text(text="-"))
        s.addElement(odf.number.Number(
                decimalplaces="0", grouping="true", minintegerdigits="1"))
        s.addElement(odf.number.Text(text=" "))
        s.addElement(odf.number.CurrencySymbol(
                text=u"€", country="DE", language="de"))
        s.addElement(odf.style.Map(
                applystylename="cs-euro-positive", condition="value()>=0"))
        self.__calcdoc.styles.addElement(s)

        # This is the one for the read-only modules
        s = odf.style.Style(name="col-euro", family="table-cell",
                            datastylename="cs-euro")
        self.__calcdoc.automaticstyles.addElement(s)
        self.doc_styles["col-euro"] = s

        # And the same for read-write.
        s = odf.style.Style(name="col-euro-rw", family="table-cell",
                            datastylename="cs-euro")
        s.addElement(odf.style.TableCellProperties(cellprotect="none",
                                                   printcontent="true"))
        self.__calcdoc.automaticstyles.addElement(s)
        self.doc_styles["col-euro-rw"] = s

    def __create_styles_int(self):
        '''Number as used for days count.'''
        s = odf.number.NumberStyle(name="ns-int")
        s.addElement(odf.number.Number(
                decimalplaces="0", minintegerdigits="1"))
        self.__calcdoc.automaticstyles.addElement(s)

        # The version for read-only.
        s = odf.style.Style(name="col-int", family="table-cell",
                            datastylename="ns-int")
        self.__calcdoc.automaticstyles.addElement(s)
        self.doc_styles["col-int"] = s

        # And the same for rw.
        s = odf.style.Style(name="col-int-rw", family="table-cell",
                            datastylename="ns-int")
        s.addElement(odf.style.TableCellProperties(cellprotect="none",
                                                   printcontent="true"))
        self.__calcdoc.automaticstyles.addElement(s)
        self.doc_styles["col-int-rw"] = s

    def __create_styles(self):
        '''There is the need to apply some styles.'''
        # There is the need for many different styles.
        self.__create_styles_table_cell()
        self.__create_styles_table_column()
        self.__create_styles_currency()
        self.__create_styles_int()

    def topic_set_pre(self, topics_set):
        '''Document setup and output.
           Because for this document a very specific sort order
           must be implemented, everything must be done here explicitly -
           the executor interface can only partially be used.'''
        self.__calcdoc = OpenDocumentSpreadsheet()
        self.__create_meta()
        self.__create_styles()

    def topic_set_post(self, topics_set):
        '''Document storage.'''
        self.__calcdoc.save(self._output_filename, True)

    # Sheet creation functions.

    def __create_costs_sheet(self, sreqs):
        sheet = odf.table.Table(name="Costs", protected="true")
        self.create_form(sheet, sreqs)
        self.create_costs_column_styles(sheet)
        self.create_costs_header(sheet, sreqs[0])
        self.create_costs_content(sheet, sreqs)
        self.__calcdoc.spreadsheet.addElement(sheet)

    def __create_deps_sheet(self, sreqs):
        sheet = odf.table.Table(name="Deps")  # , protected="true")
        self.create_reqs_ids_row(sheet, sreqs)
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
            tc = odf.table.TableCell()
            if len(req.incoming) > 0:
                # By default, the chosen is the first one.
                p = odf.text.P(text=req.incoming[0].get_id())
                tc.addElement(p)
            tr.addElement(tc)
        sheet.addElement(tr)

        self.create_empty_row(sheet)
        # Output all the dependent requirements
        self.create_deps_dependent(sheet, sreqs)
        self.__calcdoc.spreadsheet.addElement(sheet)

    def __create_sums_sheet(self, sreqs):
        self.create_one_sums_sheet(self.__calcdoc, sreqs, "SumRate", "L")
        self.create_one_sums_sheet(self.__calcdoc, sreqs, "SumMat", "M")

    def __create_constants_sheet(self):
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
        self.__calcdoc.spreadsheet.addElement(sheet)

    # This is added to get all the results in one point (sheet)
    # which makes it easier to handle the output.
    def __create_result_sheet(self, sreqs):
        sheet = odf.table.Table(name="Results", protected="true")
        i = 0
        for req in sreqs:
            tr = odf.table.TableRow()
            self.create_result_one_req(tr, req, i)
            sheet.addElement(tr)
            i += 1
        self.__calcdoc.spreadsheet.addElement(sheet)

    def requirement_set_pre(self, requirement_set):
        '''The output of all the content.'''

        # Because of a problem with the current OpenOffice versions,
        # there is the need to sometimes arrange requirements as rows
        # and sometimes as columns:
        # It is not possible to define the range of a list input as a
        # row: it must be a column.
        # The order dictionary holds the number - which can be
        # computed in a row or column.
        def create_reqs_index(srqes):
            sreqs_index = {}
            cnt = 0
            for req in sreqs:
                sreqs_index[req] = cnt
                cnt += 1
            return sreqs_index

        sreqs = topological_sort(requirement_set)

        # Create the row / column index of each requirement
        self.sreqs_index = create_reqs_index(sreqs)

        # Create and save the document
        self.__create_costs_sheet(sreqs)
        self.__create_deps_sheet(sreqs)
        self.__create_sums_sheet(sreqs)
        self.__create_constants_sheet()
        self.__create_result_sheet(sreqs)

    def cmad_topic_continuum_pre(self, _):
        '''Write out the one and only dependency to all the requirements.'''
        tracer.debug("Called.")
        CreateMakeDependencies.write_reqs_dep(self._cmad_file,
                                              self._output_filename)

    # ======================================================================
    # 2nd level functions
    #

    # helper functions

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

    # Create the first row in the deps or sums sheet: all the ids
    @staticmethod
    def create_reqs_ids_row(sheet, sreqs):
        tr = odf.table.TableRow()
        for req in sreqs:
            tc = odf.table.TableCell()
            p = odf.text.P(text=req.name)
            tc.addElement(p)
            tr.addElement(tc)
        sheet.addElement(tr)

    # Creates a text cell with the given text. Optional a style can be
    # specified.
    @staticmethod
    def create_text_cell(table_row, text, style=None):
        if style is not None:
            tc = odf.table.TableCell(stylename=style)
        else:
            tc = odf.table.TableCell()

        if text is not None:
            p = odf.text.P(text=text)
            tc.addElement(p)
        table_row.addElement(tc)

    # Functions handling costs

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
        # 15 Supplier
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-supplier"])
        sheet.addElement(tc)
        # 16 Comment
        tc = odf.table.TableColumn(stylename=self.doc_styles["col-comment"])
        sheet.addElement(tc)

    def create_costs_header(self, sheet, req):
        # First is empty
        self.create_empty_row(sheet)
        # Second holds only the Overall sum
        tr = odf.table.TableRow()
        self.create_text_cell(tr, req.get_id(),
                              self.doc_styles["tc-bold"])
        sheet.addElement(tr)
        # Followed by an additionally empty line
        self.create_empty_row(sheet)
        # Table header line 1
        tr = odf.table.TableRow()
        for h in ["Id", "Name", "Compliant", "Costs for requirement",
                  None, None, None, "Dependent from",
                  "Costs of dependent", None, None,
                  "Overall sum", None, None, "Supplier", "Comment"]:
            self.create_text_cell(tr, h, self.doc_styles["tc-bold-blue"])
        sheet.addElement(tr)
        # Table header line 2
        tr = odf.table.TableRow()
        for h in [None, None, None, "dayrate",
                  "#days", "material", "sum", None,
                  "rate", "material", "sum",
                  "rate", "material", "sum", None, None]:
            self.create_text_cell(tr, h, self.doc_styles["tc-bold-blue"])
        sheet.addElement(tr)

    def create_costs_content(self, sheet, sreqs):
        i = 0
        for req in sreqs:
            tr = odf.table.TableRow()
            self.create_costs_content_req(tr, req, i)
            sheet.addElement(tr)
            i += 1

    def create_costs_content_req(self, tr, req, i):
        choi = i + DEPS_HEADER_LEN
        # First cell is the id
        self.create_text_cell(tr, req.name)
        # Second cell is the name
        self.create_text_cell(tr, req.get_value("Name").get_content())
        # Third is the compliant
        tc = odf.table.TableCell()
        dc = odf.draw.Control(control="lbcompliant%s" % req.name,
                              zindex="0",
                              x="0.0in",
                              y="0.0in",
                              endcelladdress="Costs.C%d" % (choi + 1),
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
        if len(req.incoming) > 0:
            dc = odf.draw.Control(control="lbdependentfrom%s" % req.name,
                                  zindex="0",
                                  x="0.0in",
                                  y="0.0in",
                                  endcelladdress="Costs.H%d" % (choi + 1),
                                  endx="1.2in",
                                  endy="0.0in")
            tc.addElement(dc)
        tr.addElement(tc)

        # dependet rate and material
        # Do not do this for first cell.
        for sname in ["SumRate", "SumMat"]:
            if len(req.outgoing) > 0:
                tc = odf.table.TableCell(
                    valuetype="currency", currency="EUR",
                    formula="oooc:=SUM([%s.%s2:%s.%s%d])"
                    % (sname, self.__sscoords[i], sname, self.__sscoords[i],
                       (1 + len(req.outgoing))))
                tr.addElement(tc)
            else:
                self.create_empty_currency_cell_ro(tr)

        # sum of dependent
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.I%d]+[.J%d]" % (choi, choi))
        tr.addElement(tc)

        # Overall rate
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.D%d]*[.E%d]+[.I%d]" % (choi, choi, choi))
        tr.addElement(tc)
        # Overall material
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.F%d]+[.J%d]" % (choi, choi))
        tr.addElement(tc)
        # Overall sum
        tc = odf.table.TableCell(
            valuetype="currency", currency="EUR",
            formula="oooc:=[.L%d]+[.M%d]" % (choi, choi))
        tr.addElement(tc)
        # Supplier
        tc = odf.table.TableCell(
            valuetype="string", stylename=self.doc_styles["tc-shrink-to-fit"])
        tr.addElement(tc)
        # Comment
        tc = odf.table.TableCell(
            valuetype="string", stylename=self.doc_styles["tc-shrink-to-fit"])
        tr.addElement(tc)

    # Functions handling deps

    def create_deps_dependent(self, sheet, sreqs):
        # The number of the following rows depend on the maximum
        # number of incoming requirements.
        # This flags if there is something found with the current
        # index.
        i = 0
        while True:
            tr = odf.table.TableRow()
            index_used = False
            for req in sreqs:
                if len(req.incoming) > i:
                    tc = odf.table.TableCell()
                    p = odf.text.P(text=req.incoming[i].name)
                    tc.addElement(p)
                    tr.addElement(tc)
                    index_used = True
                else:
                    tc = odf.table.TableCell()
                    tr.addElement(tc)
            sheet.addElement(tr)
            if not index_used:
                break
            i += 1

    # Functions handling sums

    # Create one sum sheet
    def create_one_sums_sheet(self, calcdoc, sreqs, name, colname):
        sheet = odf.table.Table(name=name, protected="true")
        self.create_reqs_ids_row(sheet, sreqs)

        i = 0
        while True:
            tr = odf.table.TableRow()
            index_used = False
            for req in sreqs:
                if len(req.outgoing) > i:
                    # This is somewhat complicated:
                    # If on the Costs sheet one direction is chosen,
                    # it is written to the deps sheet (row 3).
                    # If this row contains the name of the current
                    # requirment, it is chosen to be dependent and the
                    # overall costs of that requirement must go to the
                    # local list - which then is again summed over on
                    # the cost sheet.
                    tc = odf.table.TableCell(
                        valuetype="currency", currency="EUR",
                        formula='oooc:=IF([Deps.%s3]="%s";[Costs.%s%d];0)' %
                        (self.__sscoords[self.sreqs_index[req.outgoing[i]]],
                         req.name, colname,
                         self.sreqs_index[req.outgoing[i]] + DEPS_HEADER_LEN))
                    tr.addElement(tc)
                    index_used = True
                else:
                    tc = odf.table.TableCell()
                    tr.addElement(tc)
            sheet.addElement(tr)
            if not index_used:
                break
            i += 1

        calcdoc.spreadsheet.addElement(sheet)

    # Functions handling forms
    def create_form(self, calcdoc, sreqs):
        forms = odf.office.Forms(
            applydesignmode="false",
            automaticfocus="false")
        form = odf.form.Form(
            applyfilter="true",
            commandtype="table",
            controlimplementation="ooo:com.sun.star.form.component.Form",
            name="Standard",
            targetframe="",
            href="")

        # Listboxes for compliant
        i = 0
        for req in sreqs:
            lb = odf.form.Listbox(
                id="lbcompliant%s" % req.name,
                boundcolumn="1",
                dropdown="yes",
                controlimplementation="ooo:com.sun.star."
                "form.component.ListBox",
                linkedcell="Deps.%s2" % self.__sscoords[i],
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
            defaultval = odf.form.ListValue(stringvalue='0')
            lstprop.addElement(defaultval)
            lbproperties.addElement(lstprop)

            lb.addElement(lbproperties)

            form.addElement(lb)
            i += 1

        # Listboxes for dependent from
        i = 0
        for req in sreqs:
            # When there is only one entry in the list, there is no
            # need to have a dropdown list.
            # Needed?
            # ddown = "yes"
            # if len(req.incoming) <= 1:
            #    ddown = "no"

            lb = odf.form.Listbox(
                id="lbdependentfrom%s" % req.name,
                boundcolumn="1",
                dropdown="yes",
                controlimplementation="ooo:com.sun.star."
                "form.component.ListBox",
                linkedcell="Deps.%s3" % self.__sscoords[i],
                listlinkagetype="selection",
                name="ListBox Dependet From %s" % req.name,
                size="3",
                sourcecellrange="Deps.%s5:Deps.%s%d" % (
                    self.__sscoords[i], self.__sscoords[i],
                    len(req.incoming) + 4)
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
            defaultval = odf.form.ListValue(stringvalue='0')
            lstprop.addElement(defaultval)
            lbproperties.addElement(lstprop)
            # Read only
            # When there is only one dependent requirement, it makes
            # no sense to have something which can be changed.
            # Therefore this should be readonly then.
            if len(req.incoming) <= 1:
                lstprop = odf.form.Property(
                    propertyname="ReadOnly",
                    valuetype="boolean",
                    booleanvalue="true")
                lbproperties.addElement(lstprop)

            lb.addElement(lbproperties)

            form.addElement(lb)
            i += 1

        forms.addElement(form)
        calcdoc.addElement(forms)

    # Functions handling result sheet
    def create_result_one_req(self, tr, req, i):
        # 1 Id
        self.create_text_cell(tr, req.name)
        # 2 Compliance
        tc = odf.table.TableCell(
            valuetype="string",
            formula="oooc:=[Deps.%s2]" % self.__sscoords[i])
        tr.addElement(tc)
        # Prices
        for r in ["D", "E", "F"]:
            tc = odf.table.TableCell(
                valuetype="string",
                formula="oooc:=[Costs.%s%d]" % (r, i + DEPS_HEADER_LEN))
            tr.addElement(tc)
        # Dependent from
        tc = odf.table.TableCell(
            valuetype="string",
            formula="oooc:=[Deps.%s3]" % self.__sscoords[i])
        tr.addElement(tc)
        # Supplier
        tc = odf.table.TableCell(
            valuetype="string",
            formula="oooc:=[Costs.O%d]" % (i + DEPS_HEADER_LEN))
        tr.addElement(tc)
        # Comment
        tc = odf.table.TableCell(
            valuetype="string",
            formula="oooc:=[Costs.P%d]" % (i + DEPS_HEADER_LEN))
        tr.addElement(tc)

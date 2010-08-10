#
# OpenOffice Pricing output class for rmtoo
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.TopologicalSort import topological_sort

class oopricing1:

    def __init__(self, param):
        self.topic_name = param[0]
        self.output_filename = param[1]

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
        order = {}

        cnt = 0
        for req in sreqs:
            order[req] = cnt
            cnt += 1

        self.sheet1(sreqs)
        self.formdef(sreqs)

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


    def sheet2(self, sreqs):
        # The first row are just the names.
        for req in sreqs:
            print('<table:table-cell office:value-type="string">\n'
                  '<text:p>%s</text:p>\n'
                  '</table:table-cell>' % req.name)
        print('</table:table-row>')

        # The second row is where all the results will be inserted.
        # Therefore put an empty row in.
        # The third row contains the indices of the requirement
        # which is chosen as the dependent one.
        for i in xrange(0, 2):
            print('<table:table-row table:style-name="ro1">\n'
                  '<table:table-cell table:number-columns-repeated="%d"/>\n'
                  '</table:table-row>' % len(sreqs))

        # The number of the following rows depend on the maximum
        # number of outgoing requirements.
        # This flags if there is something found with the current
        # index.
        i=0
        while True:
            print('<table:table-row table:style-name="ro1">')
            index_used=False
            for req in sreqs:
                if len(req.outgoing)>i:
                    print('<table:table-cell office:value-type="string">'
                          '<text:p>%s</text:p>'
                          '</table:table-cell>' % req.outgoing[i].name)
                    index_used=True
                else:
                    print('<table:table-cell/>')
            print('</table:table-row>')
            if not index_used:
                break
            i+=1


            #print("DSKLJSDKj %s" % order)


### rm ../clc0A.ods ; zip -v -r ../clc0A.ods .


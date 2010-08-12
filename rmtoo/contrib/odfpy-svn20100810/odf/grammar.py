# -*- coding: utf-8 -*-
# Copyright (C) 2006-2008 Søren Roug, European Environment Agency
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#

__doc__=""" In principle the OpenDocument schema converted to python structures.
Currently it contains the legal child elements of a given element.
To be used for validation check in the API
"""

from odf.namespaces import *
allowed_children = {
	(TEXTNS,u'reference-ref') : (
	),
	(TEXTNS,u'bookmark-ref') : (
	),
	(TEXTNS,u'page-count') : (
	),
	(TEXTNS,u'paragraph-count') : (
	),
	(TEXTNS,u'word-count') : (
	),
	(TEXTNS,u'character-count') : (
	),
	(TEXTNS,u'table-count') : (
	),
	(TEXTNS,u'image-count') : (
	),
	(TEXTNS,u'object-count') : (
	),
	(TEXTNS,u'alphabetical-index-mark') : (
	),
	(TEXTNS,u'alphabetical-index-mark-end') : (
	),
	(TEXTNS,u'alphabetical-index-mark-start') : (
	),
	(ANIMNS,u'animate') : (
	),
	(ANIMNS,u'animateColor') : (
	),
	(ANIMNS,u'animateMotion') : (
	),
	(ANIMNS,u'animateTransform') : (
	),
	(ANIMNS,u'audio') : (
	),
	(TEXTNS,u'author-initials') : (
	),
	(TEXTNS,u'author-name') : (
	),
	(METANS,u'auto-reload') : (
	),
	(OFFICENS,u'automatic-styles') : (
		(STYLENS,u'style'), 
		(TEXTNS,u'list-style'), 
		(NUMBERNS,u'number-style'), 
		(NUMBERNS,u'currency-style'), 
		(NUMBERNS,u'percentage-style'), 
		(NUMBERNS,u'date-style'), 
		(NUMBERNS,u'time-style'), 
		(NUMBERNS,u'boolean-style'), 
		(NUMBERNS,u'text-style'), 
		(STYLENS,u'page-layout'), 
	),
	(STYLENS,u'background-image') : (
		(OFFICENS,u'binary-data'), 
	),
	(TEXTNS,u'bibliography-mark') : (
	),
	(FORMNS,u'button') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'change') : (
	),
	(TEXTNS,u'change-end') : (
	),
	(TEXTNS,u'change-start') : (
	),
	(TEXTNS,u'chapter') : (
	),
	(OFFICENS,u'chart') : (
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TABLENS,u'calculation-settings'), 
		(TABLENS,u'content-validations'), 
		(TABLENS,u'label-ranges'), 
		(CHARTNS,u'chart'), 
		(TABLENS,u'named-expressions'), 
		(TABLENS,u'database-ranges'), 
		(TABLENS,u'data-pilot-tables'), 
		(TABLENS,u'consolidation'), 
		(TABLENS,u'dde-links'), 
	),
	(FORMNS,u'checkbox') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(STYLENS,u'columns') : (
		(STYLENS,u'column-sep'), 
		(STYLENS,u'column'), 
	),
	(FORMNS,u'combobox') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
		(FORMNS,u'item'), 
	),
	(ANIMNS,u'command') : (
		(ANIMNS,u'param'), 
	),
	(TEXTNS,u'conditional-text') : (
	),
	(TEXTNS,u'creation-date') : (
	),
	(METANS,u'creation-date') : (
	),
	(TEXTNS,u'creation-time') : (
	),
	(TEXTNS,u'creator') : (
	),
	(TEXTNS,u'database-display') : (
		(FORMNS,u'connection-resource'), 
	),
	(TEXTNS,u'database-name') : (
		(FORMNS,u'connection-resource'), 
	),
	(TEXTNS,u'database-next') : (
		(FORMNS,u'connection-resource'), 
	),
	(TEXTNS,u'database-row-number') : (
		(FORMNS,u'connection-resource'), 
	),
	(TEXTNS,u'database-row-select') : (
		(FORMNS,u'connection-resource'), 
	),
	(FORMNS,u'date') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'date') : (
	),
	(PRESENTATIONNS,u'date-time-decl') : (
	),
	(PRESENTATIONNS,u'date-time') : (
	),
	(TEXTNS,u'dde-connection-decls') : (
		(TEXTNS,u'dde-connection-decl'), 
	),
	(TEXTNS,u'dde-connection') : (
	),
	(TEXTNS,u'deletion') : (
		(OFFICENS,u'change-info'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
	),
	(TEXTNS,u'description') : (
	),
	(DCNS,u'description') : (
	),
	(METANS,u'document-statistic') : (
	),
	(OFFICENS,u'drawing') : (
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TABLENS,u'calculation-settings'), 
		(TABLENS,u'content-validations'), 
		(TABLENS,u'label-ranges'), 
		(DRAWNS,u'page'), 
		(TABLENS,u'named-expressions'), 
		(TABLENS,u'database-ranges'), 
		(TABLENS,u'data-pilot-tables'), 
		(TABLENS,u'consolidation'), 
		(TABLENS,u'dde-links'), 
	),
	(STYLENS,u'drop-cap') : (
	),
	(TEXTNS,u'editing-cycles') : (
	),
	(METANS,u'editing-cycles') : (
	),
	(TEXTNS,u'editing-duration') : (
	),
	(METANS,u'editing-duration') : (
	),
	(TEXTNS,u'execute-macro') : (
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'expression') : (
	),
	(FORMNS,u'file') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'file-name') : (
	),
	(FORMNS,u'fixed-text') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(OFFICENS,u'font-face-decls') : (
		(STYLENS,u'font-face'), 
	),
	(PRESENTATIONNS,u'footer-decl') : (
	),
	(PRESENTATIONNS,u'footer') : (
	),
	(STYLENS,u'footnote-sep') : (
	),
	(TEXTNS,u'format-change') : (
		(OFFICENS,u'change-info'), 
	),
	(FORMNS,u'formatted-text') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(OFFICENS,u'forms') : (
		(FORMNS,u'form'), 
		(XFORMSNS,u'model'), 
	),
	(FORMNS,u'frame') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(METANS,u'generator') : (
	),
	(FORMNS,u'generic-control') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(FORMNS,u'grid') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
		(FORMNS,u'column'), 
	),
	(PRESENTATIONNS,u'header-decl') : (
	),
	(PRESENTATIONNS,u'header') : (
	),
	(FORMNS,u'hidden') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'hidden-paragraph') : (
	),
	(TEXTNS,u'hidden-text') : (
	),
	(METANS,u'hyperlink-behaviour') : (
	),
	(FORMNS,u'image') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(OFFICENS,u'image') : (
		(DRAWNS,u'frame'), 
	),
	(FORMNS,u'image-frame') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'initial-creator') : (
	),
	(METANS,u'initial-creator') : (
	),
	(TEXTNS,u'insertion') : (
		(OFFICENS,u'change-info'), 
	),
	(ANIMNS,u'iterate') : (
		(ANIMNS,u'animate'), 
		(ANIMNS,u'set'), 
		(ANIMNS,u'animateMotion'), 
		(ANIMNS,u'animateColor'), 
		(ANIMNS,u'animateTransform'), 
		(ANIMNS,u'transitionFilter'), 
		(ANIMNS,u'par'), 
		(ANIMNS,u'seq'), 
		(ANIMNS,u'iterate'), 
		(ANIMNS,u'audio'), 
		(ANIMNS,u'command'), 
	),
	(METANS,u'keyword') : (
	),
	(TEXTNS,u'keywords') : (
	),
	(CHARTNS,u'label-separator') : (
		(TEXTNS,u'p'), 
	),
	(DCNS,u'language') : (
	),
	(TEXTNS,u'line-break') : (
	),
	(STYLENS,u'list-level-label-alignment') : (
	),
	(TEXTNS,u'list-level-style-bullet') : (
		(STYLENS,u'list-level-properties'), 
		(STYLENS,u'text-properties'), 
	),
	(TEXTNS,u'list-level-style-image') : (
		(OFFICENS,u'binary-data'), 
		(STYLENS,u'list-level-properties'), 
	),
	(TEXTNS,u'list-level-style-number') : (
		(STYLENS,u'list-level-properties'), 
		(STYLENS,u'text-properties'), 
	),
	(FORMNS,u'list-property') : (
		(FORMNS,u'list-value'), 
		(FORMNS,u'list-value'), 
		(FORMNS,u'list-value'), 
		(FORMNS,u'list-value'), 
		(FORMNS,u'list-value'), 
		(FORMNS,u'list-value'), 
		(FORMNS,u'list-value'), 
	),
	(FORMNS,u'list-value') : (
	),
	(FORMNS,u'list-value') : (
	),
	(FORMNS,u'list-value') : (
	),
	(FORMNS,u'list-value') : (
	),
	(FORMNS,u'list-value') : (
	),
	(FORMNS,u'list-value') : (
	),
	(FORMNS,u'list-value') : (
	),
	(FORMNS,u'listbox') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
		(FORMNS,u'option'), 
	),
	(OFFICENS,u'master-styles') : (
		(STYLENS,u'master-page'), 
		(STYLENS,u'handout-master'), 
		(DRAWNS,u'layer-set'), 
		(TABLENS,u'table-template'), 
	),
	(TEXTNS,u'measure') : (
	),
	(TEXTNS,u'meta') : (
		(TEXTNS,u's'), 
		(TEXTNS,u'tab'), 
		(TEXTNS,u'line-break'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'span'), 
		(TEXTNS,u'meta'), 
		(TEXTNS,u'bookmark'), 
		(TEXTNS,u'bookmark-start'), 
		(TEXTNS,u'bookmark-end'), 
		(TEXTNS,u'reference-mark'), 
		(TEXTNS,u'reference-mark-start'), 
		(TEXTNS,u'reference-mark-end'), 
		(TEXTNS,u'note'), 
		(TEXTNS,u'ruby'), 
		(OFFICENS,u'annotation'), 
		(OFFICENS,u'annotation-end'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'date'), 
		(TEXTNS,u'time'), 
		(TEXTNS,u'page-number'), 
		(TEXTNS,u'page-continuation'), 
		(TEXTNS,u'sender-firstname'), 
		(TEXTNS,u'sender-lastname'), 
		(TEXTNS,u'sender-initials'), 
		(TEXTNS,u'sender-title'), 
		(TEXTNS,u'sender-position'), 
		(TEXTNS,u'sender-email'), 
		(TEXTNS,u'sender-phone-private'), 
		(TEXTNS,u'sender-fax'), 
		(TEXTNS,u'sender-company'), 
		(TEXTNS,u'sender-phone-work'), 
		(TEXTNS,u'sender-street'), 
		(TEXTNS,u'sender-city'), 
		(TEXTNS,u'sender-postal-code'), 
		(TEXTNS,u'sender-country'), 
		(TEXTNS,u'sender-state-or-province'), 
		(TEXTNS,u'author-name'), 
		(TEXTNS,u'author-initials'), 
		(TEXTNS,u'chapter'), 
		(TEXTNS,u'file-name'), 
		(TEXTNS,u'template-name'), 
		(TEXTNS,u'sheet-name'), 
		(TEXTNS,u'variable-set'), 
		(TEXTNS,u'variable-get'), 
		(TEXTNS,u'variable-input'), 
		(TEXTNS,u'user-field-get'), 
		(TEXTNS,u'user-field-input'), 
		(TEXTNS,u'sequence'), 
		(TEXTNS,u'expression'), 
		(TEXTNS,u'text-input'), 
		(TEXTNS,u'initial-creator'), 
		(TEXTNS,u'creation-date'), 
		(TEXTNS,u'creation-time'), 
		(TEXTNS,u'description'), 
		(TEXTNS,u'user-defined'), 
		(TEXTNS,u'print-time'), 
		(TEXTNS,u'print-date'), 
		(TEXTNS,u'printed-by'), 
		(TEXTNS,u'title'), 
		(TEXTNS,u'subject'), 
		(TEXTNS,u'keywords'), 
		(TEXTNS,u'editing-cycles'), 
		(TEXTNS,u'editing-duration'), 
		(TEXTNS,u'modification-time'), 
		(TEXTNS,u'modification-date'), 
		(TEXTNS,u'creator'), 
		(TEXTNS,u'page-count'), 
		(TEXTNS,u'paragraph-count'), 
		(TEXTNS,u'word-count'), 
		(TEXTNS,u'character-count'), 
		(TEXTNS,u'table-count'), 
		(TEXTNS,u'image-count'), 
		(TEXTNS,u'object-count'), 
		(TEXTNS,u'database-display'), 
		(TEXTNS,u'database-next'), 
		(TEXTNS,u'database-row-select'), 
		(TEXTNS,u'database-row-number'), 
		(TEXTNS,u'database-name'), 
		(TEXTNS,u'page-variable-set'), 
		(TEXTNS,u'page-variable-get'), 
		(TEXTNS,u'placeholder'), 
		(TEXTNS,u'conditional-text'), 
		(TEXTNS,u'hidden-text'), 
		(TEXTNS,u'reference-ref'), 
		(TEXTNS,u'bookmark-ref'), 
		(TEXTNS,u'note-ref'), 
		(TEXTNS,u'sequence-ref'), 
		(TEXTNS,u'script'), 
		(TEXTNS,u'execute-macro'), 
		(TEXTNS,u'hidden-paragraph'), 
		(TEXTNS,u'dde-connection'), 
		(TEXTNS,u'measure'), 
		(TEXTNS,u'table-formula'), 
		(TEXTNS,u'meta-field'), 
		(TEXTNS,u'toc-mark-start'), 
		(TEXTNS,u'toc-mark-end'), 
		(TEXTNS,u'toc-mark'), 
		(TEXTNS,u'user-index-mark-start'), 
		(TEXTNS,u'user-index-mark-end'), 
		(TEXTNS,u'user-index-mark'), 
		(TEXTNS,u'alphabetical-index-mark-start'), 
		(TEXTNS,u'alphabetical-index-mark-end'), 
		(TEXTNS,u'alphabetical-index-mark'), 
		(TEXTNS,u'bibliography-mark'), 
		(PRESENTATIONNS,u'header'), 
		(PRESENTATIONNS,u'footer'), 
		(PRESENTATIONNS,u'date-time'), 
		(TEXTNS,u'a'), 
	),
	(OFFICENS,u'meta') : (
		(METANS,u'generator'), 
		(DCNS,u'title'), 
		(DCNS,u'description'), 
		(DCNS,u'subject'), 
		(METANS,u'keyword'), 
		(METANS,u'initial-creator'), 
		(DCNS,u'creator'), 
		(METANS,u'printed-by'), 
		(METANS,u'creation-date'), 
		(DCNS,u'date'), 
		(METANS,u'print-date'), 
		(METANS,u'template'), 
		(METANS,u'auto-reload'), 
		(METANS,u'hyperlink-behaviour'), 
		(DCNS,u'language'), 
		(METANS,u'editing-cycles'), 
		(METANS,u'editing-duration'), 
		(METANS,u'document-statistic'), 
		(METANS,u'user-defined'), 
	),
	(TEXTNS,u'meta-field') : (
		(TEXTNS,u's'), 
		(TEXTNS,u'tab'), 
		(TEXTNS,u'line-break'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'span'), 
		(TEXTNS,u'meta'), 
		(TEXTNS,u'bookmark'), 
		(TEXTNS,u'bookmark-start'), 
		(TEXTNS,u'bookmark-end'), 
		(TEXTNS,u'reference-mark'), 
		(TEXTNS,u'reference-mark-start'), 
		(TEXTNS,u'reference-mark-end'), 
		(TEXTNS,u'note'), 
		(TEXTNS,u'ruby'), 
		(OFFICENS,u'annotation'), 
		(OFFICENS,u'annotation-end'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'date'), 
		(TEXTNS,u'time'), 
		(TEXTNS,u'page-number'), 
		(TEXTNS,u'page-continuation'), 
		(TEXTNS,u'sender-firstname'), 
		(TEXTNS,u'sender-lastname'), 
		(TEXTNS,u'sender-initials'), 
		(TEXTNS,u'sender-title'), 
		(TEXTNS,u'sender-position'), 
		(TEXTNS,u'sender-email'), 
		(TEXTNS,u'sender-phone-private'), 
		(TEXTNS,u'sender-fax'), 
		(TEXTNS,u'sender-company'), 
		(TEXTNS,u'sender-phone-work'), 
		(TEXTNS,u'sender-street'), 
		(TEXTNS,u'sender-city'), 
		(TEXTNS,u'sender-postal-code'), 
		(TEXTNS,u'sender-country'), 
		(TEXTNS,u'sender-state-or-province'), 
		(TEXTNS,u'author-name'), 
		(TEXTNS,u'author-initials'), 
		(TEXTNS,u'chapter'), 
		(TEXTNS,u'file-name'), 
		(TEXTNS,u'template-name'), 
		(TEXTNS,u'sheet-name'), 
		(TEXTNS,u'variable-set'), 
		(TEXTNS,u'variable-get'), 
		(TEXTNS,u'variable-input'), 
		(TEXTNS,u'user-field-get'), 
		(TEXTNS,u'user-field-input'), 
		(TEXTNS,u'sequence'), 
		(TEXTNS,u'expression'), 
		(TEXTNS,u'text-input'), 
		(TEXTNS,u'initial-creator'), 
		(TEXTNS,u'creation-date'), 
		(TEXTNS,u'creation-time'), 
		(TEXTNS,u'description'), 
		(TEXTNS,u'user-defined'), 
		(TEXTNS,u'print-time'), 
		(TEXTNS,u'print-date'), 
		(TEXTNS,u'printed-by'), 
		(TEXTNS,u'title'), 
		(TEXTNS,u'subject'), 
		(TEXTNS,u'keywords'), 
		(TEXTNS,u'editing-cycles'), 
		(TEXTNS,u'editing-duration'), 
		(TEXTNS,u'modification-time'), 
		(TEXTNS,u'modification-date'), 
		(TEXTNS,u'creator'), 
		(TEXTNS,u'page-count'), 
		(TEXTNS,u'paragraph-count'), 
		(TEXTNS,u'word-count'), 
		(TEXTNS,u'character-count'), 
		(TEXTNS,u'table-count'), 
		(TEXTNS,u'image-count'), 
		(TEXTNS,u'object-count'), 
		(TEXTNS,u'database-display'), 
		(TEXTNS,u'database-next'), 
		(TEXTNS,u'database-row-select'), 
		(TEXTNS,u'database-row-number'), 
		(TEXTNS,u'database-name'), 
		(TEXTNS,u'page-variable-set'), 
		(TEXTNS,u'page-variable-get'), 
		(TEXTNS,u'placeholder'), 
		(TEXTNS,u'conditional-text'), 
		(TEXTNS,u'hidden-text'), 
		(TEXTNS,u'reference-ref'), 
		(TEXTNS,u'bookmark-ref'), 
		(TEXTNS,u'note-ref'), 
		(TEXTNS,u'sequence-ref'), 
		(TEXTNS,u'script'), 
		(TEXTNS,u'execute-macro'), 
		(TEXTNS,u'hidden-paragraph'), 
		(TEXTNS,u'dde-connection'), 
		(TEXTNS,u'measure'), 
		(TEXTNS,u'table-formula'), 
		(TEXTNS,u'meta-field'), 
		(TEXTNS,u'toc-mark-start'), 
		(TEXTNS,u'toc-mark-end'), 
		(TEXTNS,u'toc-mark'), 
		(TEXTNS,u'user-index-mark-start'), 
		(TEXTNS,u'user-index-mark-end'), 
		(TEXTNS,u'user-index-mark'), 
		(TEXTNS,u'alphabetical-index-mark-start'), 
		(TEXTNS,u'alphabetical-index-mark-end'), 
		(TEXTNS,u'alphabetical-index-mark'), 
		(TEXTNS,u'bibliography-mark'), 
		(PRESENTATIONNS,u'header'), 
		(PRESENTATIONNS,u'footer'), 
		(PRESENTATIONNS,u'date-time'), 
		(TEXTNS,u'a'), 
	),
	(TEXTNS,u'modification-date') : (
	),
	(TEXTNS,u'modification-time') : (
	),
	(TEXTNS,u'note-body') : (
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
	),
	(TEXTNS,u'note-citation') : (
	),
	(TEXTNS,u'note-continuation-notice-backward') : (
	),
	(TEXTNS,u'note-continuation-notice-forward') : (
	),
	(TEXTNS,u'note') : (
		(TEXTNS,u'note-citation'), 
		(TEXTNS,u'note-body'), 
	),
	(TEXTNS,u'note-ref') : (
	),
	(FORMNS,u'number') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'page-continuation') : (
	),
	(TEXTNS,u'page-number') : (
	),
	(TEXTNS,u'page-variable-get') : (
	),
	(TEXTNS,u'page-variable-set') : (
	),
	(ANIMNS,u'par') : (
		(ANIMNS,u'animate'), 
		(ANIMNS,u'set'), 
		(ANIMNS,u'animateMotion'), 
		(ANIMNS,u'animateColor'), 
		(ANIMNS,u'animateTransform'), 
		(ANIMNS,u'transitionFilter'), 
		(ANIMNS,u'par'), 
		(ANIMNS,u'seq'), 
		(ANIMNS,u'iterate'), 
		(ANIMNS,u'audio'), 
		(ANIMNS,u'command'), 
	),
	(ANIMNS,u'param') : (
	),
	(FORMNS,u'password') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'placeholder') : (
	),
	(OFFICENS,u'presentation') : (
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TABLENS,u'calculation-settings'), 
		(TABLENS,u'content-validations'), 
		(TABLENS,u'label-ranges'), 
		(PRESENTATIONNS,u'header-decl'), 
		(PRESENTATIONNS,u'footer-decl'), 
		(PRESENTATIONNS,u'date-time-decl'), 
		(DRAWNS,u'page'), 
		(PRESENTATIONNS,u'settings'), 
		(TABLENS,u'named-expressions'), 
		(TABLENS,u'database-ranges'), 
		(TABLENS,u'data-pilot-tables'), 
		(TABLENS,u'consolidation'), 
		(TABLENS,u'dde-links'), 
	),
	(METANS,u'print-date') : (
	),
	(TEXTNS,u'print-date') : (
	),
	(TEXTNS,u'print-time') : (
	),
	(METANS,u'printed-by') : (
	),
	(TEXTNS,u'printed-by') : (
	),
	(FORMNS,u'property') : (
	),
	(FORMNS,u'radio') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'reference-mark') : (
	),
	(TEXTNS,u'reference-mark-end') : (
	),
	(TEXTNS,u'reference-mark-start') : (
	),
	(TEXTNS,u'ruby-base') : (
		(TEXTNS,u's'), 
		(TEXTNS,u'tab'), 
		(TEXTNS,u'line-break'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'span'), 
		(TEXTNS,u'meta'), 
		(TEXTNS,u'bookmark'), 
		(TEXTNS,u'bookmark-start'), 
		(TEXTNS,u'bookmark-end'), 
		(TEXTNS,u'reference-mark'), 
		(TEXTNS,u'reference-mark-start'), 
		(TEXTNS,u'reference-mark-end'), 
		(TEXTNS,u'note'), 
		(TEXTNS,u'ruby'), 
		(OFFICENS,u'annotation'), 
		(OFFICENS,u'annotation-end'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'date'), 
		(TEXTNS,u'time'), 
		(TEXTNS,u'page-number'), 
		(TEXTNS,u'page-continuation'), 
		(TEXTNS,u'sender-firstname'), 
		(TEXTNS,u'sender-lastname'), 
		(TEXTNS,u'sender-initials'), 
		(TEXTNS,u'sender-title'), 
		(TEXTNS,u'sender-position'), 
		(TEXTNS,u'sender-email'), 
		(TEXTNS,u'sender-phone-private'), 
		(TEXTNS,u'sender-fax'), 
		(TEXTNS,u'sender-company'), 
		(TEXTNS,u'sender-phone-work'), 
		(TEXTNS,u'sender-street'), 
		(TEXTNS,u'sender-city'), 
		(TEXTNS,u'sender-postal-code'), 
		(TEXTNS,u'sender-country'), 
		(TEXTNS,u'sender-state-or-province'), 
		(TEXTNS,u'author-name'), 
		(TEXTNS,u'author-initials'), 
		(TEXTNS,u'chapter'), 
		(TEXTNS,u'file-name'), 
		(TEXTNS,u'template-name'), 
		(TEXTNS,u'sheet-name'), 
		(TEXTNS,u'variable-set'), 
		(TEXTNS,u'variable-get'), 
		(TEXTNS,u'variable-input'), 
		(TEXTNS,u'user-field-get'), 
		(TEXTNS,u'user-field-input'), 
		(TEXTNS,u'sequence'), 
		(TEXTNS,u'expression'), 
		(TEXTNS,u'text-input'), 
		(TEXTNS,u'initial-creator'), 
		(TEXTNS,u'creation-date'), 
		(TEXTNS,u'creation-time'), 
		(TEXTNS,u'description'), 
		(TEXTNS,u'user-defined'), 
		(TEXTNS,u'print-time'), 
		(TEXTNS,u'print-date'), 
		(TEXTNS,u'printed-by'), 
		(TEXTNS,u'title'), 
		(TEXTNS,u'subject'), 
		(TEXTNS,u'keywords'), 
		(TEXTNS,u'editing-cycles'), 
		(TEXTNS,u'editing-duration'), 
		(TEXTNS,u'modification-time'), 
		(TEXTNS,u'modification-date'), 
		(TEXTNS,u'creator'), 
		(TEXTNS,u'page-count'), 
		(TEXTNS,u'paragraph-count'), 
		(TEXTNS,u'word-count'), 
		(TEXTNS,u'character-count'), 
		(TEXTNS,u'table-count'), 
		(TEXTNS,u'image-count'), 
		(TEXTNS,u'object-count'), 
		(TEXTNS,u'database-display'), 
		(TEXTNS,u'database-next'), 
		(TEXTNS,u'database-row-select'), 
		(TEXTNS,u'database-row-number'), 
		(TEXTNS,u'database-name'), 
		(TEXTNS,u'page-variable-set'), 
		(TEXTNS,u'page-variable-get'), 
		(TEXTNS,u'placeholder'), 
		(TEXTNS,u'conditional-text'), 
		(TEXTNS,u'hidden-text'), 
		(TEXTNS,u'reference-ref'), 
		(TEXTNS,u'bookmark-ref'), 
		(TEXTNS,u'note-ref'), 
		(TEXTNS,u'sequence-ref'), 
		(TEXTNS,u'script'), 
		(TEXTNS,u'execute-macro'), 
		(TEXTNS,u'hidden-paragraph'), 
		(TEXTNS,u'dde-connection'), 
		(TEXTNS,u'measure'), 
		(TEXTNS,u'table-formula'), 
		(TEXTNS,u'meta-field'), 
		(TEXTNS,u'toc-mark-start'), 
		(TEXTNS,u'toc-mark-end'), 
		(TEXTNS,u'toc-mark'), 
		(TEXTNS,u'user-index-mark-start'), 
		(TEXTNS,u'user-index-mark-end'), 
		(TEXTNS,u'user-index-mark'), 
		(TEXTNS,u'alphabetical-index-mark-start'), 
		(TEXTNS,u'alphabetical-index-mark-end'), 
		(TEXTNS,u'alphabetical-index-mark'), 
		(TEXTNS,u'bibliography-mark'), 
		(PRESENTATIONNS,u'header'), 
		(PRESENTATIONNS,u'footer'), 
		(PRESENTATIONNS,u'date-time'), 
		(TEXTNS,u'a'), 
	),
	(TEXTNS,u'ruby') : (
		(TEXTNS,u'ruby-base'), 
		(TEXTNS,u'ruby-text'), 
	),
	(TEXTNS,u'ruby-text') : (
	),
	(TEXTNS,u's') : (
	),
	(TEXTNS,u'script') : (
	),
	(OFFICENS,u'scripts') : (
		(OFFICENS,u'script'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'sender-city') : (
	),
	(TEXTNS,u'sender-company') : (
	),
	(TEXTNS,u'sender-country') : (
	),
	(TEXTNS,u'sender-email') : (
	),
	(TEXTNS,u'sender-fax') : (
	),
	(TEXTNS,u'sender-firstname') : (
	),
	(TEXTNS,u'sender-initials') : (
	),
	(TEXTNS,u'sender-lastname') : (
	),
	(TEXTNS,u'sender-phone-private') : (
	),
	(TEXTNS,u'sender-phone-work') : (
	),
	(TEXTNS,u'sender-position') : (
	),
	(TEXTNS,u'sender-postal-code') : (
	),
	(TEXTNS,u'sender-state-or-province') : (
	),
	(TEXTNS,u'sender-street') : (
	),
	(TEXTNS,u'sender-title') : (
	),
	(ANIMNS,u'seq') : (
		(ANIMNS,u'animate'), 
		(ANIMNS,u'set'), 
		(ANIMNS,u'animateMotion'), 
		(ANIMNS,u'animateColor'), 
		(ANIMNS,u'animateTransform'), 
		(ANIMNS,u'transitionFilter'), 
		(ANIMNS,u'par'), 
		(ANIMNS,u'seq'), 
		(ANIMNS,u'iterate'), 
		(ANIMNS,u'audio'), 
		(ANIMNS,u'command'), 
	),
	(TEXTNS,u'sequence-decls') : (
		(TEXTNS,u'sequence-decl'), 
	),
	(TEXTNS,u'sequence') : (
	),
	(TEXTNS,u'sequence-ref') : (
	),
	(ANIMNS,u'set') : (
	),
	(PRESENTATIONNS,u'settings') : (
		(PRESENTATIONNS,u'show'), 
	),
	(OFFICENS,u'settings') : (
		(CONFIGNS,u'config-item-set'), 
	),
	(TEXTNS,u'sheet-name') : (
	),
	(TEXTNS,u'span') : (
		(TEXTNS,u's'), 
		(TEXTNS,u'tab'), 
		(TEXTNS,u'line-break'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'span'), 
		(TEXTNS,u'meta'), 
		(TEXTNS,u'bookmark'), 
		(TEXTNS,u'bookmark-start'), 
		(TEXTNS,u'bookmark-end'), 
		(TEXTNS,u'reference-mark'), 
		(TEXTNS,u'reference-mark-start'), 
		(TEXTNS,u'reference-mark-end'), 
		(TEXTNS,u'note'), 
		(TEXTNS,u'ruby'), 
		(OFFICENS,u'annotation'), 
		(OFFICENS,u'annotation-end'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'date'), 
		(TEXTNS,u'time'), 
		(TEXTNS,u'page-number'), 
		(TEXTNS,u'page-continuation'), 
		(TEXTNS,u'sender-firstname'), 
		(TEXTNS,u'sender-lastname'), 
		(TEXTNS,u'sender-initials'), 
		(TEXTNS,u'sender-title'), 
		(TEXTNS,u'sender-position'), 
		(TEXTNS,u'sender-email'), 
		(TEXTNS,u'sender-phone-private'), 
		(TEXTNS,u'sender-fax'), 
		(TEXTNS,u'sender-company'), 
		(TEXTNS,u'sender-phone-work'), 
		(TEXTNS,u'sender-street'), 
		(TEXTNS,u'sender-city'), 
		(TEXTNS,u'sender-postal-code'), 
		(TEXTNS,u'sender-country'), 
		(TEXTNS,u'sender-state-or-province'), 
		(TEXTNS,u'author-name'), 
		(TEXTNS,u'author-initials'), 
		(TEXTNS,u'chapter'), 
		(TEXTNS,u'file-name'), 
		(TEXTNS,u'template-name'), 
		(TEXTNS,u'sheet-name'), 
		(TEXTNS,u'variable-set'), 
		(TEXTNS,u'variable-get'), 
		(TEXTNS,u'variable-input'), 
		(TEXTNS,u'user-field-get'), 
		(TEXTNS,u'user-field-input'), 
		(TEXTNS,u'sequence'), 
		(TEXTNS,u'expression'), 
		(TEXTNS,u'text-input'), 
		(TEXTNS,u'initial-creator'), 
		(TEXTNS,u'creation-date'), 
		(TEXTNS,u'creation-time'), 
		(TEXTNS,u'description'), 
		(TEXTNS,u'user-defined'), 
		(TEXTNS,u'print-time'), 
		(TEXTNS,u'print-date'), 
		(TEXTNS,u'printed-by'), 
		(TEXTNS,u'title'), 
		(TEXTNS,u'subject'), 
		(TEXTNS,u'keywords'), 
		(TEXTNS,u'editing-cycles'), 
		(TEXTNS,u'editing-duration'), 
		(TEXTNS,u'modification-time'), 
		(TEXTNS,u'modification-date'), 
		(TEXTNS,u'creator'), 
		(TEXTNS,u'page-count'), 
		(TEXTNS,u'paragraph-count'), 
		(TEXTNS,u'word-count'), 
		(TEXTNS,u'character-count'), 
		(TEXTNS,u'table-count'), 
		(TEXTNS,u'image-count'), 
		(TEXTNS,u'object-count'), 
		(TEXTNS,u'database-display'), 
		(TEXTNS,u'database-next'), 
		(TEXTNS,u'database-row-select'), 
		(TEXTNS,u'database-row-number'), 
		(TEXTNS,u'database-name'), 
		(TEXTNS,u'page-variable-set'), 
		(TEXTNS,u'page-variable-get'), 
		(TEXTNS,u'placeholder'), 
		(TEXTNS,u'conditional-text'), 
		(TEXTNS,u'hidden-text'), 
		(TEXTNS,u'reference-ref'), 
		(TEXTNS,u'bookmark-ref'), 
		(TEXTNS,u'note-ref'), 
		(TEXTNS,u'sequence-ref'), 
		(TEXTNS,u'script'), 
		(TEXTNS,u'execute-macro'), 
		(TEXTNS,u'hidden-paragraph'), 
		(TEXTNS,u'dde-connection'), 
		(TEXTNS,u'measure'), 
		(TEXTNS,u'table-formula'), 
		(TEXTNS,u'meta-field'), 
		(TEXTNS,u'toc-mark-start'), 
		(TEXTNS,u'toc-mark-end'), 
		(TEXTNS,u'toc-mark'), 
		(TEXTNS,u'user-index-mark-start'), 
		(TEXTNS,u'user-index-mark-end'), 
		(TEXTNS,u'user-index-mark'), 
		(TEXTNS,u'alphabetical-index-mark-start'), 
		(TEXTNS,u'alphabetical-index-mark-end'), 
		(TEXTNS,u'alphabetical-index-mark'), 
		(TEXTNS,u'bibliography-mark'), 
		(PRESENTATIONNS,u'header'), 
		(PRESENTATIONNS,u'footer'), 
		(PRESENTATIONNS,u'date-time'), 
		(TEXTNS,u'a'), 
	),
	(OFFICENS,u'spreadsheet') : (
		(TABLENS,u'tracked-changes'), 
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TABLENS,u'calculation-settings'), 
		(TABLENS,u'content-validations'), 
		(TABLENS,u'label-ranges'), 
		(TABLENS,u'table'), 
		(TABLENS,u'named-expressions'), 
		(TABLENS,u'database-ranges'), 
		(TABLENS,u'data-pilot-tables'), 
		(TABLENS,u'consolidation'), 
		(TABLENS,u'dde-links'), 
	),
	(OFFICENS,u'styles') : (
		(STYLENS,u'style'), 
		(TEXTNS,u'list-style'), 
		(NUMBERNS,u'number-style'), 
		(NUMBERNS,u'currency-style'), 
		(NUMBERNS,u'percentage-style'), 
		(NUMBERNS,u'date-style'), 
		(NUMBERNS,u'time-style'), 
		(NUMBERNS,u'boolean-style'), 
		(NUMBERNS,u'text-style'), 
		(STYLENS,u'default-style'), 
		(STYLENS,u'default-page-layout'), 
		(TEXTNS,u'outline-style'), 
		(TEXTNS,u'notes-configuration'), 
		(TEXTNS,u'bibliography-configuration'), 
		(TEXTNS,u'linenumbering-configuration'), 
		(DRAWNS,u'gradient'), 
		(SVGNS,u'linearGradient'), 
		(SVGNS,u'radialGradient'), 
		(DRAWNS,u'hatch'), 
		(DRAWNS,u'fill-image'), 
		(DRAWNS,u'marker'), 
		(DRAWNS,u'stroke-dash'), 
		(DRAWNS,u'opacity'), 
		(STYLENS,u'presentation-page-layout'), 
	),
	(DCNS,u'subject') : (
	),
	(TEXTNS,u'subject') : (
	),
	(CHARTNS,u'symbol-image') : (
	),
	(TEXTNS,u'tab') : (
	),
	(STYLENS,u'tab-stops') : (
		(STYLENS,u'tab-stop'), 
	),
	(TEXTNS,u'table-formula') : (
	),
	(METANS,u'template') : (
	),
	(TEXTNS,u'template-name') : (
	),
	(FORMNS,u'text') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(OFFICENS,u'text') : (
		(OFFICENS,u'forms'), 
		(TEXTNS,u'tracked-changes'), 
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TABLENS,u'calculation-settings'), 
		(TABLENS,u'content-validations'), 
		(TABLENS,u'label-ranges'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(TEXTNS,u'page-sequence'), 
		(TABLENS,u'named-expressions'), 
		(TABLENS,u'database-ranges'), 
		(TABLENS,u'data-pilot-tables'), 
		(TABLENS,u'consolidation'), 
		(TABLENS,u'dde-links'), 
	),
	(TEXTNS,u'text-input') : (
	),
	(FORMNS,u'textarea') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
		(TEXTNS,u'p'), 
	),
	(FORMNS,u'time') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'time') : (
	),
	(DCNS,u'title') : (
	),
	(TEXTNS,u'title') : (
	),
	(TEXTNS,u'toc-mark') : (
	),
	(TEXTNS,u'toc-mark-end') : (
	),
	(TEXTNS,u'toc-mark-start') : (
	),
	(TEXTNS,u'tracked-changes') : (
		(TEXTNS,u'changed-region'), 
	),
	(ANIMNS,u'transitionFilter') : (
	),
	(TEXTNS,u'user-defined') : (
	),
	(METANS,u'user-defined') : (
	),
	(TEXTNS,u'user-field-decls') : (
		(TEXTNS,u'user-field-decl'), 
	),
	(TEXTNS,u'user-field-get') : (
	),
	(TEXTNS,u'user-field-input') : (
	),
	(TEXTNS,u'user-index-mark') : (
	),
	(TEXTNS,u'user-index-mark-end') : (
	),
	(TEXTNS,u'user-index-mark-start') : (
	),
	(FORMNS,u'value-range') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TEXTNS,u'variable-decls') : (
		(TEXTNS,u'variable-decl'), 
	),
	(TEXTNS,u'variable-get') : (
	),
	(TEXTNS,u'variable-input') : (
	),
	(TEXTNS,u'variable-set') : (
	),
	(MANIFESTNS,u'algorithm') : (
	),
	(CHARTNS,u'axis') : (
		(CHARTNS,u'title'), 
		(CHARTNS,u'categories'), 
		(CHARTNS,u'grid'), 
	),
	(CHARTNS,u'categories') : (
	),
	(CHARTNS,u'chart') : (
		(CHARTNS,u'title'), 
		(CHARTNS,u'subtitle'), 
		(CHARTNS,u'footer'), 
		(CHARTNS,u'legend'), 
		(CHARTNS,u'plot-area'), 
		(TABLENS,u'table'), 
	),
	(CHARTNS,u'data-label') : (
		(TEXTNS,u'p'), 
	),
	(CHARTNS,u'data-point') : (
		(CHARTNS,u'data-label'), 
	),
	(CHARTNS,u'domain') : (
	),
	(CHARTNS,u'equation') : (
		(TEXTNS,u'p'), 
	),
	(CHARTNS,u'error-indicator') : (
	),
	(CHARTNS,u'floor') : (
	),
	(CHARTNS,u'footer') : (
		(TEXTNS,u'p'), 
	),
	(CHARTNS,u'grid') : (
	),
	(CHARTNS,u'legend') : (
		(TEXTNS,u'p'), 
	),
	(CHARTNS,u'mean-value') : (
	),
	(CHARTNS,u'plot-area') : (
		(DR3DNS,u'light'), 
		(CHARTNS,u'axis'), 
		(CHARTNS,u'series'), 
		(CHARTNS,u'stock-gain-marker'), 
		(CHARTNS,u'stock-loss-marker'), 
		(CHARTNS,u'stock-range-line'), 
		(CHARTNS,u'wall'), 
		(CHARTNS,u'floor'), 
	),
	(CHARTNS,u'regression-curve') : (
		(CHARTNS,u'equation'), 
	),
	(CHARTNS,u'series') : (
		(CHARTNS,u'domain'), 
		(CHARTNS,u'mean-value'), 
		(CHARTNS,u'regression-curve'), 
		(CHARTNS,u'error-indicator'), 
		(CHARTNS,u'data-point'), 
		(CHARTNS,u'data-label'), 
	),
	(CHARTNS,u'stock-gain-marker') : (
	),
	(CHARTNS,u'stock-loss-marker') : (
	),
	(CHARTNS,u'stock-range-line') : (
	),
	(CHARTNS,u'subtitle') : (
		(TEXTNS,u'p'), 
	),
	(CHARTNS,u'title') : (
		(TEXTNS,u'p'), 
	),
	(CHARTNS,u'wall') : (
	),
	(CONFIGNS,u'config-item') : (
	),
	(CONFIGNS,u'config-item-map-entry') : (
		(CONFIGNS,u'config-item'), 
		(CONFIGNS,u'config-item-set'), 
		(CONFIGNS,u'config-item-map-named'), 
		(CONFIGNS,u'config-item-map-indexed'), 
	),
	(CONFIGNS,u'config-item-map-indexed') : (
		(CONFIGNS,u'config-item-map-entry'), 
	),
	(CONFIGNS,u'config-item-map-named') : (
		(CONFIGNS,u'config-item-map-entry'), 
	),
	(CONFIGNS,u'config-item-set') : (
		(CONFIGNS,u'config-item'), 
		(CONFIGNS,u'config-item-set'), 
		(CONFIGNS,u'config-item-map-named'), 
		(CONFIGNS,u'config-item-map-indexed'), 
	),
	(DBNS,u'application-connection-settings') : (
		(DBNS,u'table-filter'), 
		(DBNS,u'table-type-filter'), 
		(DBNS,u'data-source-settings'), 
	),
	(DBNS,u'auto-increment') : (
	),
	(DBNS,u'character-set') : (
	),
	(DBNS,u'column-definition') : (
	),
	(DBNS,u'column-definitions') : (
		(DBNS,u'column-definition'), 
	),
	(DBNS,u'column') : (
	),
	(DBNS,u'columns') : (
		(DBNS,u'column'), 
	),
	(DBNS,u'component-collection') : (
		(DBNS,u'component'), 
		(DBNS,u'component-collection'), 
	),
	(DBNS,u'component') : (
		(OFFICENS,u'document'), 
		(MATHNS,u'math'), 
	),
	(DBNS,u'connection-data') : (
		(DBNS,u'database-description'), 
		(DBNS,u'connection-resource'), 
		(DBNS,u'login'), 
	),
	(DBNS,u'connection-resource') : (
	),
	(DBNS,u'data-source') : (
		(DBNS,u'connection-data'), 
		(DBNS,u'driver-settings'), 
		(DBNS,u'application-connection-settings'), 
	),
	(DBNS,u'data-source-setting') : (
		(DBNS,u'data-source-setting-value'), 
	),
	(DBNS,u'data-source-setting-value') : (
	),
	(DBNS,u'data-source-settings') : (
		(DBNS,u'data-source-setting'), 
	),
	(DBNS,u'database-description') : (
		(DBNS,u'file-based-database'), 
		(DBNS,u'server-database'), 
	),
	(DBNS,u'delimiter') : (
	),
	(DBNS,u'driver-settings') : (
		(DBNS,u'auto-increment'), 
		(DBNS,u'delimiter'), 
		(DBNS,u'character-set'), 
		(DBNS,u'table-settings'), 
	),
	(DBNS,u'file-based-database') : (
	),
	(DBNS,u'filter-statement') : (
	),
	(DBNS,u'forms') : (
		(DBNS,u'component'), 
		(DBNS,u'component-collection'), 
	),
	(DBNS,u'index-column') : (
	),
	(DBNS,u'index-columns') : (
		(DBNS,u'index-column'), 
	),
	(DBNS,u'index') : (
		(DBNS,u'index-columns'), 
	),
	(DBNS,u'indices') : (
		(DBNS,u'index'), 
	),
	(DBNS,u'key-column') : (
	),
	(DBNS,u'key-columns') : (
		(DBNS,u'key-column'), 
	),
	(DBNS,u'key') : (
		(DBNS,u'key-columns'), 
	),
	(DBNS,u'keys') : (
		(DBNS,u'key'), 
	),
	(DBNS,u'login') : (
	),
	(DBNS,u'order-statement') : (
	),
	(DBNS,u'queries') : (
		(DBNS,u'query'), 
		(DBNS,u'query-collection'), 
	),
	(DBNS,u'query-collection') : (
		(DBNS,u'query'), 
		(DBNS,u'query-collection'), 
	),
	(DBNS,u'query') : (
		(DBNS,u'order-statement'), 
		(DBNS,u'filter-statement'), 
		(DBNS,u'columns'), 
		(DBNS,u'update-table'), 
	),
	(DBNS,u'reports') : (
		(DBNS,u'component'), 
		(DBNS,u'component-collection'), 
	),
	(DBNS,u'schema-definition') : (
		(DBNS,u'table-definitions'), 
	),
	(DBNS,u'server-database') : (
	),
	(DBNS,u'table-definition') : (
		(DBNS,u'column-definitions'), 
		(DBNS,u'keys'), 
		(DBNS,u'indices'), 
	),
	(DBNS,u'table-definitions') : (
		(DBNS,u'table-definition'), 
	),
	(DBNS,u'table-exclude-filter') : (
		(DBNS,u'table-filter-pattern'), 
	),
	(DBNS,u'table-filter') : (
		(DBNS,u'table-include-filter'), 
		(DBNS,u'table-exclude-filter'), 
	),
	(DBNS,u'table-filter-pattern') : (
	),
	(DBNS,u'table-include-filter') : (
		(DBNS,u'table-filter-pattern'), 
	),
	(DBNS,u'table-representation') : (
		(DBNS,u'order-statement'), 
		(DBNS,u'filter-statement'), 
		(DBNS,u'columns'), 
	),
	(DBNS,u'table-representations') : (
		(DBNS,u'table-representation'), 
	),
	(DBNS,u'table-setting') : (
		(DBNS,u'delimiter'), 
		(DBNS,u'character-set'), 
	),
	(DBNS,u'table-settings') : (
		(DBNS,u'table-setting'), 
	),
	(DBNS,u'table-type-filter') : (
		(DBNS,u'table-type'), 
	),
	(DBNS,u'table-type') : (
	),
	(DBNS,u'update-table') : (
	),
	(DCNS,u'creator') : (
	),
	(DCNS,u'date') : (
	),
	(DR3DNS,u'cube') : (
	),
	(DR3DNS,u'extrude') : (
	),
	(DR3DNS,u'light') : (
	),
	(DR3DNS,u'rotate') : (
	),
	(DR3DNS,u'scene') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(DR3DNS,u'light'), 
		(DR3DNS,u'scene'), 
		(DR3DNS,u'extrude'), 
		(DR3DNS,u'sphere'), 
		(DR3DNS,u'rotate'), 
		(DR3DNS,u'cube'), 
		(DRAWNS,u'glue-point'), 
	),
	(DR3DNS,u'sphere') : (
	),
	(DRAWNS,u'a') : (
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
	),
	(DRAWNS,u'applet') : (
		(DRAWNS,u'param'), 
	),
	(DRAWNS,u'area-circle') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
	),
	(DRAWNS,u'area-polygon') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
	),
	(DRAWNS,u'area-rectangle') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
	),
	(DRAWNS,u'caption') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'circle') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'connector') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'contour-path') : (
	),
	(DRAWNS,u'contour-polygon') : (
	),
	(DRAWNS,u'control') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(DRAWNS,u'glue-point'), 
	),
	(DRAWNS,u'custom-shape') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(DRAWNS,u'enhanced-geometry'), 
	),
	(DRAWNS,u'ellipse') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'enhanced-geometry') : (
		(DRAWNS,u'equation'), 
		(DRAWNS,u'handle'), 
	),
	(DRAWNS,u'equation') : (
	),
	(DRAWNS,u'fill-image') : (
	),
	(DRAWNS,u'floating-frame') : (
	),
	(DRAWNS,u'frame') : (
		(DRAWNS,u'text-box'), 
		(DRAWNS,u'image'), 
		(DRAWNS,u'object'), 
		(DRAWNS,u'object-ole'), 
		(DRAWNS,u'applet'), 
		(DRAWNS,u'floating-frame'), 
		(DRAWNS,u'plugin'), 
		(TABLENS,u'table'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(DRAWNS,u'image-map'), 
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(DRAWNS,u'contour-polygon'), 
		(DRAWNS,u'contour-path'), 
	),
	(DRAWNS,u'g') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
	),
	(DRAWNS,u'glue-point') : (
	),
	(DRAWNS,u'gradient') : (
	),
	(DRAWNS,u'handle') : (
	),
	(DRAWNS,u'hatch') : (
	),
	(DRAWNS,u'image') : (
		(OFFICENS,u'binary-data'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'image-map') : (
		(DRAWNS,u'area-rectangle'), 
		(DRAWNS,u'area-circle'), 
		(DRAWNS,u'area-polygon'), 
	),
	(DRAWNS,u'layer') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
	),
	(DRAWNS,u'layer-set') : (
		(DRAWNS,u'layer'), 
	),
	(DRAWNS,u'line') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'marker') : (
	),
	(DRAWNS,u'measure') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'object') : (
		(OFFICENS,u'document'), 
		(MATHNS,u'math'), 
	),
	(DRAWNS,u'object-ole') : (
		(OFFICENS,u'binary-data'), 
	),
	(DRAWNS,u'opacity') : (
	),
	(DRAWNS,u'page') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(DRAWNS,u'layer-set'), 
		(OFFICENS,u'forms'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(PRESENTATIONNS,u'animations'), 
		(ANIMNS,u'animate'), 
		(ANIMNS,u'set'), 
		(ANIMNS,u'animateMotion'), 
		(ANIMNS,u'animateColor'), 
		(ANIMNS,u'animateTransform'), 
		(ANIMNS,u'transitionFilter'), 
		(ANIMNS,u'par'), 
		(ANIMNS,u'seq'), 
		(ANIMNS,u'iterate'), 
		(ANIMNS,u'audio'), 
		(ANIMNS,u'command'), 
		(PRESENTATIONNS,u'notes'), 
	),
	(DRAWNS,u'page-thumbnail') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
	),
	(DRAWNS,u'param') : (
	),
	(DRAWNS,u'path') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'plugin') : (
		(DRAWNS,u'param'), 
	),
	(DRAWNS,u'polygon') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'polyline') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'rect') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'regular-polygon') : (
		(SVGNS,u'title'), 
		(SVGNS,u'desc'), 
		(OFFICENS,u'event-listeners'), 
		(DRAWNS,u'glue-point'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(DRAWNS,u'stroke-dash') : (
	),
	(DRAWNS,u'text-box') : (
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
	),
	(MANIFESTNS,u'encryption-data') : (
		(MANIFESTNS,u'algorithm'), 
		(MANIFESTNS,u'start-key-generation'), 
		(MANIFESTNS,u'key-derivation'), 
	),
	(MANIFESTNS,u'file-entry') : (
		(MANIFESTNS,u'encryption-data'), 
	),
	(FORMNS,u'column') : (
		(FORMNS,u'text'), 
		(FORMNS,u'textarea'), 
		(FORMNS,u'formatted-text'), 
		(FORMNS,u'number'), 
		(FORMNS,u'date'), 
		(FORMNS,u'time'), 
		(FORMNS,u'combobox'), 
		(FORMNS,u'listbox'), 
		(FORMNS,u'checkbox'), 
	),
	(FORMNS,u'connection-resource') : (
	),
	(FORMNS,u'form') : (
		(FORMNS,u'properties'), 
		(OFFICENS,u'event-listeners'), 
		(FORMNS,u'text'), 
		(FORMNS,u'textarea'), 
		(FORMNS,u'formatted-text'), 
		(FORMNS,u'number'), 
		(FORMNS,u'date'), 
		(FORMNS,u'time'), 
		(FORMNS,u'combobox'), 
		(FORMNS,u'listbox'), 
		(FORMNS,u'checkbox'), 
		(FORMNS,u'password'), 
		(FORMNS,u'file'), 
		(FORMNS,u'fixed-text'), 
		(FORMNS,u'button'), 
		(FORMNS,u'image'), 
		(FORMNS,u'radio'), 
		(FORMNS,u'frame'), 
		(FORMNS,u'image-frame'), 
		(FORMNS,u'hidden'), 
		(FORMNS,u'grid'), 
		(FORMNS,u'value-range'), 
		(FORMNS,u'generic-control'), 
		(FORMNS,u'form'), 
		(FORMNS,u'connection-resource'), 
	),
	(FORMNS,u'item') : (
	),
	(FORMNS,u'option') : (
	),
	(FORMNS,u'properties') : (
		(FORMNS,u'property'), 
		(FORMNS,u'list-property'), 
	),
	(MANIFESTNS,u'key-derivation') : (
	),
	(MANIFESTNS,u'manifest') : (
		(MANIFESTNS,u'file-entry'), 
	),
	(MATHNS,u'math') : 
		None,
	(METANS,u'date-string') : (
	),
	(NUMBERNS,u'am-pm') : (
	),
	(NUMBERNS,u'boolean') : (
	),
	(NUMBERNS,u'boolean-style') : (
		(STYLENS,u'text-properties'), 
		(NUMBERNS,u'text'), 
		(NUMBERNS,u'boolean'), 
		(STYLENS,u'map'), 
	),
	(NUMBERNS,u'currency-style') : (
		(STYLENS,u'text-properties'), 
		(NUMBERNS,u'text'), 
		(NUMBERNS,u'number'), 
		(NUMBERNS,u'currency-symbol'), 
		(STYLENS,u'map'), 
	),
	(NUMBERNS,u'currency-symbol') : (
	),
	(NUMBERNS,u'date-style') : (
		(STYLENS,u'text-properties'), 
		(NUMBERNS,u'text'), 
		(NUMBERNS,u'day'), 
		(NUMBERNS,u'month'), 
		(NUMBERNS,u'year'), 
		(NUMBERNS,u'era'), 
		(NUMBERNS,u'day-of-week'), 
		(NUMBERNS,u'week-of-year'), 
		(NUMBERNS,u'quarter'), 
		(NUMBERNS,u'hours'), 
		(NUMBERNS,u'am-pm'), 
		(NUMBERNS,u'minutes'), 
		(NUMBERNS,u'seconds'), 
		(STYLENS,u'map'), 
	),
	(NUMBERNS,u'day') : (
	),
	(NUMBERNS,u'day-of-week') : (
	),
	(NUMBERNS,u'embedded-text') : (
	),
	(NUMBERNS,u'era') : (
	),
	(NUMBERNS,u'fraction') : (
	),
	(NUMBERNS,u'hours') : (
	),
	(NUMBERNS,u'minutes') : (
	),
	(NUMBERNS,u'month') : (
	),
	(NUMBERNS,u'number') : (
		(NUMBERNS,u'embedded-text'), 
	),
	(NUMBERNS,u'number-style') : (
		(STYLENS,u'text-properties'), 
		(NUMBERNS,u'text'), 
		(NUMBERNS,u'number'), 
		(NUMBERNS,u'scientific-number'), 
		(NUMBERNS,u'fraction'), 
		(STYLENS,u'map'), 
	),
	(NUMBERNS,u'percentage-style') : (
		(STYLENS,u'text-properties'), 
		(NUMBERNS,u'text'), 
		(NUMBERNS,u'number'), 
		(STYLENS,u'map'), 
	),
	(NUMBERNS,u'quarter') : (
	),
	(NUMBERNS,u'scientific-number') : (
	),
	(NUMBERNS,u'seconds') : (
	),
	(NUMBERNS,u'text-content') : (
	),
	(NUMBERNS,u'text') : (
	),
	(NUMBERNS,u'text-style') : (
		(STYLENS,u'text-properties'), 
		(NUMBERNS,u'text'), 
		(NUMBERNS,u'text-content'), 
		(STYLENS,u'map'), 
	),
	(NUMBERNS,u'time-style') : (
		(STYLENS,u'text-properties'), 
		(NUMBERNS,u'text'), 
		(NUMBERNS,u'hours'), 
		(NUMBERNS,u'am-pm'), 
		(NUMBERNS,u'minutes'), 
		(NUMBERNS,u'seconds'), 
		(STYLENS,u'map'), 
	),
	(NUMBERNS,u'week-of-year') : (
	),
	(NUMBERNS,u'year') : (
	),
	(OFFICENS,u'annotation-end') : (
	),
	(OFFICENS,u'annotation') : (
		(DCNS,u'creator'), 
		(DCNS,u'date'), 
		(METANS,u'date-string'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
	),
	(OFFICENS,u'binary-data') : (
	),
	(OFFICENS,u'body') : (
		(OFFICENS,u'text'), 
		(OFFICENS,u'drawing'), 
		(OFFICENS,u'presentation'), 
		(OFFICENS,u'spreadsheet'), 
		(OFFICENS,u'chart'), 
		(OFFICENS,u'image'), 
		(OFFICENS,u'database'), 
	),
	(OFFICENS,u'change-info') : (
		(DCNS,u'creator'), 
		(DCNS,u'date'), 
		(TEXTNS,u'p'), 
	),
	(OFFICENS,u'database') : (
		(DBNS,u'data-source'), 
		(DBNS,u'forms'), 
		(DBNS,u'reports'), 
		(DBNS,u'queries'), 
		(DBNS,u'table-representations'), 
		(DBNS,u'schema-definition'), 
	),
	(OFFICENS,u'dde-source') : (
	),
	(OFFICENS,u'document-content') : (
		(OFFICENS,u'scripts'), 
		(OFFICENS,u'font-face-decls'), 
		(OFFICENS,u'automatic-styles'), 
		(OFFICENS,u'body'), 
	),
	(OFFICENS,u'document') : (
		(OFFICENS,u'meta'), 
		(OFFICENS,u'settings'), 
		(OFFICENS,u'scripts'), 
		(OFFICENS,u'font-face-decls'), 
		(OFFICENS,u'styles'), 
		(OFFICENS,u'automatic-styles'), 
		(OFFICENS,u'master-styles'), 
		(OFFICENS,u'body'), 
	),
	(OFFICENS,u'document-meta') : (
		(OFFICENS,u'meta'), 
	),
	(OFFICENS,u'document-settings') : (
		(OFFICENS,u'settings'), 
	),
	(OFFICENS,u'document-styles') : (
		(OFFICENS,u'font-face-decls'), 
		(OFFICENS,u'styles'), 
		(OFFICENS,u'automatic-styles'), 
		(OFFICENS,u'master-styles'), 
	),
	(OFFICENS,u'event-listeners') : (
		(SCRIPTNS,u'event-listener'), 
		(PRESENTATIONNS,u'event-listener'), 
	),
	(OFFICENS,u'script') : 
		None,
	(PRESENTATIONNS,u'animation-group') : (
		(PRESENTATIONNS,u'show-shape'), 
		(PRESENTATIONNS,u'show-text'), 
		(PRESENTATIONNS,u'hide-shape'), 
		(PRESENTATIONNS,u'hide-text'), 
		(PRESENTATIONNS,u'dim'), 
		(PRESENTATIONNS,u'play'), 
	),
	(PRESENTATIONNS,u'animations') : (
		(PRESENTATIONNS,u'show-shape'), 
		(PRESENTATIONNS,u'show-text'), 
		(PRESENTATIONNS,u'hide-shape'), 
		(PRESENTATIONNS,u'hide-text'), 
		(PRESENTATIONNS,u'dim'), 
		(PRESENTATIONNS,u'play'), 
		(PRESENTATIONNS,u'animation-group'), 
	),
	(PRESENTATIONNS,u'dim') : (
		(PRESENTATIONNS,u'sound'), 
	),
	(PRESENTATIONNS,u'event-listener') : (
		(PRESENTATIONNS,u'sound'), 
	),
	(PRESENTATIONNS,u'hide-shape') : (
		(PRESENTATIONNS,u'sound'), 
	),
	(PRESENTATIONNS,u'hide-text') : (
		(PRESENTATIONNS,u'sound'), 
	),
	(PRESENTATIONNS,u'notes') : (
		(OFFICENS,u'forms'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
	),
	(PRESENTATIONNS,u'placeholder') : (
	),
	(PRESENTATIONNS,u'play') : (
	),
	(PRESENTATIONNS,u'show') : (
	),
	(PRESENTATIONNS,u'show-shape') : (
		(PRESENTATIONNS,u'sound'), 
	),
	(PRESENTATIONNS,u'show-text') : (
		(PRESENTATIONNS,u'sound'), 
	),
	(PRESENTATIONNS,u'sound') : (
	),
	(SCRIPTNS,u'event-listener') : (
	),
	(MANIFESTNS,u'start-key-generation') : (
	),
	(STYLENS,u'chart-properties') : (
		(CHARTNS,u'symbol-image'), 
		(CHARTNS,u'label-separator'), 
	),
	(STYLENS,u'column') : (
	),
	(STYLENS,u'column-sep') : (
	),
	(STYLENS,u'default-page-layout') : (
		(STYLENS,u'page-layout-properties'), 
		(STYLENS,u'header-style'), 
		(STYLENS,u'footer-style'), 
	),
	(STYLENS,u'default-style') : (
		(STYLENS,u'text-properties'), 
		(STYLENS,u'paragraph-properties'), 
		(STYLENS,u'section-properties'), 
		(STYLENS,u'ruby-properties'), 
		(STYLENS,u'table-properties'), 
		(STYLENS,u'table-column-properties'), 
		(STYLENS,u'table-row-properties'), 
		(STYLENS,u'table-cell-properties'), 
		(STYLENS,u'graphic-properties'), 
		(STYLENS,u'drawing-page-properties'), 
		(STYLENS,u'chart-properties'), 
	),
	(STYLENS,u'drawing-page-properties') : (
		(PRESENTATIONNS,u'sound'), 
	),
	(STYLENS,u'font-face') : (
		(SVGNS,u'font-face-src'), 
		(SVGNS,u'definition-src'), 
	),
	(STYLENS,u'footer') : (
		(TEXTNS,u'tracked-changes'), 
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(TEXTNS,u'index-title'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(STYLENS,u'region-left'), 
		(STYLENS,u'region-center'), 
		(STYLENS,u'region-right'), 
	),
	(STYLENS,u'footer-left') : (
		(TEXTNS,u'tracked-changes'), 
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(TEXTNS,u'index-title'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(STYLENS,u'region-left'), 
		(STYLENS,u'region-center'), 
		(STYLENS,u'region-right'), 
	),
	(STYLENS,u'footer-style') : (
		(STYLENS,u'header-footer-properties'), 
	),
	(STYLENS,u'graphic-properties') : (
		(TEXTNS,u'list-style'), 
		(STYLENS,u'background-image'), 
		(STYLENS,u'columns'), 
	),
	(STYLENS,u'handout-master') : (
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
	),
	(STYLENS,u'header-footer-properties') : (
		(STYLENS,u'background-image'), 
	),
	(STYLENS,u'header') : (
		(TEXTNS,u'tracked-changes'), 
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(TEXTNS,u'index-title'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(STYLENS,u'region-left'), 
		(STYLENS,u'region-center'), 
		(STYLENS,u'region-right'), 
	),
	(STYLENS,u'header-left') : (
		(TEXTNS,u'tracked-changes'), 
		(TEXTNS,u'variable-decls'), 
		(TEXTNS,u'sequence-decls'), 
		(TEXTNS,u'user-field-decls'), 
		(TEXTNS,u'dde-connection-decls'), 
		(TEXTNS,u'alphabetical-index-auto-mark-file'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(TEXTNS,u'index-title'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(STYLENS,u'region-left'), 
		(STYLENS,u'region-center'), 
		(STYLENS,u'region-right'), 
	),
	(STYLENS,u'header-style') : (
		(STYLENS,u'header-footer-properties'), 
	),
	(STYLENS,u'list-level-properties') : (
		(STYLENS,u'list-level-label-alignment'), 
	),
	(STYLENS,u'map') : (
	),
	(STYLENS,u'master-page') : (
		(STYLENS,u'header'), 
		(STYLENS,u'header-left'), 
		(STYLENS,u'footer'), 
		(STYLENS,u'footer-left'), 
		(DRAWNS,u'layer-set'), 
		(OFFICENS,u'forms'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(ANIMNS,u'animate'), 
		(ANIMNS,u'set'), 
		(ANIMNS,u'animateMotion'), 
		(ANIMNS,u'animateColor'), 
		(ANIMNS,u'animateTransform'), 
		(ANIMNS,u'transitionFilter'), 
		(ANIMNS,u'par'), 
		(ANIMNS,u'seq'), 
		(ANIMNS,u'iterate'), 
		(ANIMNS,u'audio'), 
		(ANIMNS,u'command'), 
		(PRESENTATIONNS,u'notes'), 
	),
	(STYLENS,u'page-layout') : (
		(STYLENS,u'page-layout-properties'), 
		(STYLENS,u'header-style'), 
		(STYLENS,u'footer-style'), 
	),
	(STYLENS,u'page-layout-properties') : (
		(STYLENS,u'background-image'), 
		(STYLENS,u'columns'), 
		(STYLENS,u'footnote-sep'), 
	),
	(STYLENS,u'paragraph-properties') : (
		(STYLENS,u'tab-stops'), 
		(STYLENS,u'drop-cap'), 
		(STYLENS,u'background-image'), 
	),
	(STYLENS,u'presentation-page-layout') : (
		(PRESENTATIONNS,u'placeholder'), 
	),
	(STYLENS,u'region-center') : (
		(TEXTNS,u'p'), 
	),
	(STYLENS,u'region-left') : (
		(TEXTNS,u'p'), 
	),
	(STYLENS,u'region-right') : (
		(TEXTNS,u'p'), 
	),
	(STYLENS,u'ruby-properties') : (
	),
	(STYLENS,u'section-properties') : (
		(STYLENS,u'background-image'), 
		(STYLENS,u'columns'), 
		(TEXTNS,u'notes-configuration'), 
	),
	(STYLENS,u'style') : (
		(STYLENS,u'text-properties'), 
		(STYLENS,u'paragraph-properties'), 
		(STYLENS,u'section-properties'), 
		(STYLENS,u'ruby-properties'), 
		(STYLENS,u'table-properties'), 
		(STYLENS,u'table-column-properties'), 
		(STYLENS,u'table-row-properties'), 
		(STYLENS,u'table-cell-properties'), 
		(STYLENS,u'graphic-properties'), 
		(STYLENS,u'drawing-page-properties'), 
		(STYLENS,u'chart-properties'), 
		(STYLENS,u'map'), 
	),
	(STYLENS,u'tab-stop') : (
	),
	(STYLENS,u'table-cell-properties') : (
		(STYLENS,u'background-image'), 
	),
	(STYLENS,u'table-column-properties') : (
	),
	(STYLENS,u'table-properties') : (
		(STYLENS,u'background-image'), 
	),
	(STYLENS,u'table-row-properties') : (
		(STYLENS,u'background-image'), 
	),
	(STYLENS,u'text-properties') : (
	),
	(SVGNS,u'definition-src') : (
	),
	(SVGNS,u'desc') : (
	),
	(SVGNS,u'font-face-format') : (
	),
	(SVGNS,u'font-face-name') : (
	),
	(SVGNS,u'font-face-src') : (
		(SVGNS,u'font-face-uri'), 
		(SVGNS,u'font-face-name'), 
	),
	(SVGNS,u'font-face-uri') : (
		(SVGNS,u'font-face-format'), 
	),
	(SVGNS,u'linearGradient') : (
		(SVGNS,u'stop'), 
	),
	(SVGNS,u'radialGradient') : (
		(SVGNS,u'stop'), 
	),
	(SVGNS,u'stop') : (
	),
	(SVGNS,u'title') : (
	),
	(TABLENS,u'background') : (
	),
	(TABLENS,u'body') : (
	),
	(TABLENS,u'calculation-settings') : (
		(TABLENS,u'null-date'), 
		(TABLENS,u'iteration'), 
	),
	(TABLENS,u'cell-address') : (
	),
	(TABLENS,u'cell-content-change') : (
		(TABLENS,u'cell-address'), 
		(OFFICENS,u'change-info'), 
		(TABLENS,u'dependencies'), 
		(TABLENS,u'deletions'), 
		(TABLENS,u'previous'), 
	),
	(TABLENS,u'cell-content-deletion') : (
		(TABLENS,u'cell-address'), 
		(TABLENS,u'change-track-table-cell'), 
	),
	(TABLENS,u'cell-range-source') : (
	),
	(TABLENS,u'change-deletion') : (
	),
	(TABLENS,u'change-track-table-cell') : (
		(TEXTNS,u'p'), 
	),
	(TABLENS,u'consolidation') : (
	),
	(TABLENS,u'content-validation') : (
		(TABLENS,u'help-message'), 
		(TABLENS,u'error-message'), 
		(TABLENS,u'error-macro'), 
		(OFFICENS,u'event-listeners'), 
	),
	(TABLENS,u'content-validations') : (
		(TABLENS,u'content-validation'), 
	),
	(TABLENS,u'covered-table-cell') : (
		(TABLENS,u'cell-range-source'), 
		(OFFICENS,u'annotation'), 
		(TABLENS,u'detective'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
	),
	(TABLENS,u'cut-offs') : (
		(TABLENS,u'movement-cut-off'), 
		(TABLENS,u'insertion-cut-off'), 
	),
	(TABLENS,u'data-pilot-display-info') : (
	),
	(TABLENS,u'data-pilot-field') : (
		(TABLENS,u'data-pilot-level'), 
		(TABLENS,u'data-pilot-field-reference'), 
		(TABLENS,u'data-pilot-groups'), 
	),
	(TABLENS,u'data-pilot-field-reference') : (
	),
	(TABLENS,u'data-pilot-group') : (
		(TABLENS,u'data-pilot-group-member'), 
	),
	(TABLENS,u'data-pilot-group-member') : (
	),
	(TABLENS,u'data-pilot-groups') : (
		(TABLENS,u'data-pilot-group'), 
	),
	(TABLENS,u'data-pilot-layout-info') : (
	),
	(TABLENS,u'data-pilot-level') : (
		(TABLENS,u'data-pilot-subtotals'), 
		(TABLENS,u'data-pilot-members'), 
		(TABLENS,u'data-pilot-display-info'), 
		(TABLENS,u'data-pilot-sort-info'), 
		(TABLENS,u'data-pilot-layout-info'), 
	),
	(TABLENS,u'data-pilot-member') : (
	),
	(TABLENS,u'data-pilot-members') : (
		(TABLENS,u'data-pilot-member'), 
	),
	(TABLENS,u'data-pilot-sort-info') : (
	),
	(TABLENS,u'data-pilot-subtotal') : (
	),
	(TABLENS,u'data-pilot-subtotals') : (
		(TABLENS,u'data-pilot-subtotal'), 
	),
	(TABLENS,u'data-pilot-table') : (
		(TABLENS,u'database-source-sql'), 
		(TABLENS,u'database-source-query'), 
		(TABLENS,u'database-source-table'), 
		(TABLENS,u'source-service'), 
		(TABLENS,u'source-cell-range'), 
		(TABLENS,u'data-pilot-field'), 
	),
	(TABLENS,u'data-pilot-tables') : (
		(TABLENS,u'data-pilot-table'), 
	),
	(TABLENS,u'database-range') : (
		(TABLENS,u'database-source-sql'), 
		(TABLENS,u'database-source-query'), 
		(TABLENS,u'database-source-table'), 
		(TABLENS,u'filter'), 
		(TABLENS,u'sort'), 
		(TABLENS,u'subtotal-rules'), 
	),
	(TABLENS,u'database-ranges') : (
		(TABLENS,u'database-range'), 
	),
	(TABLENS,u'database-source-table') : (
	),
	(TABLENS,u'database-source-sql') : (
	),
	(TABLENS,u'database-source-query') : (
	),
	(TABLENS,u'dde-link') : (
		(OFFICENS,u'dde-source'), 
		(TABLENS,u'table'), 
	),
	(TABLENS,u'dde-links') : (
		(TABLENS,u'dde-link'), 
	),
	(TABLENS,u'deletion') : (
		(OFFICENS,u'change-info'), 
		(TABLENS,u'dependencies'), 
		(TABLENS,u'deletions'), 
		(TABLENS,u'cut-offs'), 
	),
	(TABLENS,u'deletions') : (
		(TABLENS,u'cell-content-deletion'), 
		(TABLENS,u'change-deletion'), 
	),
	(TABLENS,u'dependencies') : (
		(TABLENS,u'dependency'), 
	),
	(TABLENS,u'dependency') : (
	),
	(TABLENS,u'desc') : (
	),
	(TABLENS,u'detective') : (
		(TABLENS,u'highlighted-range'), 
		(TABLENS,u'operation'), 
	),
	(TABLENS,u'error-macro') : (
	),
	(TABLENS,u'error-message') : (
		(TEXTNS,u'p'), 
	),
	(TABLENS,u'even-columns') : (
	),
	(TABLENS,u'even-rows') : (
	),
	(TABLENS,u'filter-and') : (
		(TABLENS,u'filter-or'), 
		(TABLENS,u'filter-condition'), 
	),
	(TABLENS,u'filter-condition') : (
		(TABLENS,u'filter-set-item'), 
	),
	(TABLENS,u'filter') : (
		(TABLENS,u'filter-condition'), 
		(TABLENS,u'filter-and'), 
		(TABLENS,u'filter-or'), 
	),
	(TABLENS,u'filter-or') : (
		(TABLENS,u'filter-and'), 
		(TABLENS,u'filter-condition'), 
	),
	(TABLENS,u'filter-set-item') : (
	),
	(TABLENS,u'first-column') : (
	),
	(TABLENS,u'first-row') : (
	),
	(TABLENS,u'help-message') : (
		(TEXTNS,u'p'), 
	),
	(TABLENS,u'highlighted-range') : (
	),
	(TABLENS,u'insertion-cut-off') : (
	),
	(TABLENS,u'insertion') : (
		(OFFICENS,u'change-info'), 
		(TABLENS,u'dependencies'), 
		(TABLENS,u'deletions'), 
	),
	(TABLENS,u'iteration') : (
	),
	(TABLENS,u'label-range') : (
	),
	(TABLENS,u'label-ranges') : (
		(TABLENS,u'label-range'), 
	),
	(TABLENS,u'last-column') : (
	),
	(TABLENS,u'last-row') : (
	),
	(TABLENS,u'movement-cut-off') : (
	),
	(TABLENS,u'movement') : (
		(TABLENS,u'source-range-address'), 
		(TABLENS,u'target-range-address'), 
		(OFFICENS,u'change-info'), 
		(TABLENS,u'dependencies'), 
		(TABLENS,u'deletions'), 
	),
	(TABLENS,u'named-expression') : (
	),
	(TABLENS,u'named-expressions') : (
		(TABLENS,u'named-range'), 
		(TABLENS,u'named-expression'), 
	),
	(TABLENS,u'named-range') : (
	),
	(TABLENS,u'null-date') : (
	),
	(TABLENS,u'odd-columns') : (
	),
	(TABLENS,u'odd-rows') : (
	),
	(TABLENS,u'operation') : (
	),
	(TABLENS,u'previous') : (
		(TABLENS,u'change-track-table-cell'), 
	),
	(TABLENS,u'scenario') : (
	),
	(TABLENS,u'shapes') : (
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
	),
	(TABLENS,u'sort-by') : (
	),
	(TABLENS,u'sort-groups') : (
	),
	(TABLENS,u'sort') : (
		(TABLENS,u'sort-by'), 
	),
	(TABLENS,u'source-cell-range') : (
		(TABLENS,u'filter'), 
	),
	(TABLENS,u'source-range-address') : (
	),
	(TABLENS,u'source-service') : (
	),
	(TABLENS,u'subtotal-field') : (
	),
	(TABLENS,u'subtotal-rule') : (
		(TABLENS,u'subtotal-field'), 
	),
	(TABLENS,u'subtotal-rules') : (
		(TABLENS,u'sort-groups'), 
		(TABLENS,u'subtotal-rule'), 
	),
	(TABLENS,u'table-cell') : (
		(TABLENS,u'cell-range-source'), 
		(OFFICENS,u'annotation'), 
		(TABLENS,u'detective'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
	),
	(TABLENS,u'table-column-group') : (
		(TABLENS,u'table-column-group'), 
		(TABLENS,u'table-columns'), 
		(TABLENS,u'table-column'), 
		(TABLENS,u'table-header-columns'), 
	),
	(TABLENS,u'table-column') : (
	),
	(TABLENS,u'table-columns') : (
		(TABLENS,u'table-column'), 
	),
	(TABLENS,u'table-header-columns') : (
		(TABLENS,u'table-column'), 
	),
	(TABLENS,u'table-header-rows') : (
		(TEXTNS,u'soft-page-break'), 
		(TABLENS,u'table-row'), 
	),
	(TABLENS,u'table') : (
		(TABLENS,u'title'), 
		(TABLENS,u'desc'), 
		(TABLENS,u'table-source'), 
		(OFFICENS,u'dde-source'), 
		(TABLENS,u'scenario'), 
		(OFFICENS,u'forms'), 
		(TABLENS,u'shapes'), 
		(TABLENS,u'table-column-group'), 
		(TABLENS,u'table-columns'), 
		(TABLENS,u'table-column'), 
		(TABLENS,u'table-header-columns'), 
		(TABLENS,u'table-row-group'), 
		(TABLENS,u'table-rows'), 
		(TEXTNS,u'soft-page-break'), 
		(TABLENS,u'table-row'), 
		(TABLENS,u'table-header-rows'), 
		(TABLENS,u'named-expressions'), 
	),
	(TABLENS,u'table-row-group') : (
		(TABLENS,u'table-row-group'), 
		(TABLENS,u'table-rows'), 
		(TEXTNS,u'soft-page-break'), 
		(TABLENS,u'table-row'), 
		(TABLENS,u'table-header-rows'), 
	),
	(TABLENS,u'table-row') : (
		(TABLENS,u'table-cell'), 
		(TABLENS,u'covered-table-cell'), 
	),
	(TABLENS,u'table-rows') : (
		(TEXTNS,u'soft-page-break'), 
		(TABLENS,u'table-row'), 
	),
	(TABLENS,u'table-source') : (
	),
	(TABLENS,u'table-template') : (
		(TABLENS,u'first-row'), 
		(TABLENS,u'last-row'), 
		(TABLENS,u'first-column'), 
		(TABLENS,u'last-column'), 
		(TABLENS,u'body'), 
		(TABLENS,u'even-rows'), 
		(TABLENS,u'odd-rows'), 
		(TABLENS,u'even-columns'), 
		(TABLENS,u'odd-columns'), 
		(TABLENS,u'background'), 
	),
	(TABLENS,u'target-range-address') : (
	),
	(TABLENS,u'title') : (
	),
	(TABLENS,u'tracked-changes') : (
		(TABLENS,u'cell-content-change'), 
		(TABLENS,u'insertion'), 
		(TABLENS,u'deletion'), 
		(TABLENS,u'movement'), 
	),
	(TEXTNS,u'a') : (
		(OFFICENS,u'event-listeners'), 
		(TEXTNS,u's'), 
		(TEXTNS,u'tab'), 
		(TEXTNS,u'line-break'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'span'), 
		(TEXTNS,u'meta'), 
		(TEXTNS,u'bookmark'), 
		(TEXTNS,u'bookmark-start'), 
		(TEXTNS,u'bookmark-end'), 
		(TEXTNS,u'reference-mark'), 
		(TEXTNS,u'reference-mark-start'), 
		(TEXTNS,u'reference-mark-end'), 
		(TEXTNS,u'note'), 
		(TEXTNS,u'ruby'), 
		(OFFICENS,u'annotation'), 
		(OFFICENS,u'annotation-end'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'date'), 
		(TEXTNS,u'time'), 
		(TEXTNS,u'page-number'), 
		(TEXTNS,u'page-continuation'), 
		(TEXTNS,u'sender-firstname'), 
		(TEXTNS,u'sender-lastname'), 
		(TEXTNS,u'sender-initials'), 
		(TEXTNS,u'sender-title'), 
		(TEXTNS,u'sender-position'), 
		(TEXTNS,u'sender-email'), 
		(TEXTNS,u'sender-phone-private'), 
		(TEXTNS,u'sender-fax'), 
		(TEXTNS,u'sender-company'), 
		(TEXTNS,u'sender-phone-work'), 
		(TEXTNS,u'sender-street'), 
		(TEXTNS,u'sender-city'), 
		(TEXTNS,u'sender-postal-code'), 
		(TEXTNS,u'sender-country'), 
		(TEXTNS,u'sender-state-or-province'), 
		(TEXTNS,u'author-name'), 
		(TEXTNS,u'author-initials'), 
		(TEXTNS,u'chapter'), 
		(TEXTNS,u'file-name'), 
		(TEXTNS,u'template-name'), 
		(TEXTNS,u'sheet-name'), 
		(TEXTNS,u'variable-set'), 
		(TEXTNS,u'variable-get'), 
		(TEXTNS,u'variable-input'), 
		(TEXTNS,u'user-field-get'), 
		(TEXTNS,u'user-field-input'), 
		(TEXTNS,u'sequence'), 
		(TEXTNS,u'expression'), 
		(TEXTNS,u'text-input'), 
		(TEXTNS,u'initial-creator'), 
		(TEXTNS,u'creation-date'), 
		(TEXTNS,u'creation-time'), 
		(TEXTNS,u'description'), 
		(TEXTNS,u'user-defined'), 
		(TEXTNS,u'print-time'), 
		(TEXTNS,u'print-date'), 
		(TEXTNS,u'printed-by'), 
		(TEXTNS,u'title'), 
		(TEXTNS,u'subject'), 
		(TEXTNS,u'keywords'), 
		(TEXTNS,u'editing-cycles'), 
		(TEXTNS,u'editing-duration'), 
		(TEXTNS,u'modification-time'), 
		(TEXTNS,u'modification-date'), 
		(TEXTNS,u'creator'), 
		(TEXTNS,u'page-count'), 
		(TEXTNS,u'paragraph-count'), 
		(TEXTNS,u'word-count'), 
		(TEXTNS,u'character-count'), 
		(TEXTNS,u'table-count'), 
		(TEXTNS,u'image-count'), 
		(TEXTNS,u'object-count'), 
		(TEXTNS,u'database-display'), 
		(TEXTNS,u'database-next'), 
		(TEXTNS,u'database-row-select'), 
		(TEXTNS,u'database-row-number'), 
		(TEXTNS,u'database-name'), 
		(TEXTNS,u'page-variable-set'), 
		(TEXTNS,u'page-variable-get'), 
		(TEXTNS,u'placeholder'), 
		(TEXTNS,u'conditional-text'), 
		(TEXTNS,u'hidden-text'), 
		(TEXTNS,u'reference-ref'), 
		(TEXTNS,u'bookmark-ref'), 
		(TEXTNS,u'note-ref'), 
		(TEXTNS,u'sequence-ref'), 
		(TEXTNS,u'script'), 
		(TEXTNS,u'execute-macro'), 
		(TEXTNS,u'hidden-paragraph'), 
		(TEXTNS,u'dde-connection'), 
		(TEXTNS,u'measure'), 
		(TEXTNS,u'table-formula'), 
		(TEXTNS,u'meta-field'), 
		(TEXTNS,u'toc-mark-start'), 
		(TEXTNS,u'toc-mark-end'), 
		(TEXTNS,u'toc-mark'), 
		(TEXTNS,u'user-index-mark-start'), 
		(TEXTNS,u'user-index-mark-end'), 
		(TEXTNS,u'user-index-mark'), 
		(TEXTNS,u'alphabetical-index-mark-start'), 
		(TEXTNS,u'alphabetical-index-mark-end'), 
		(TEXTNS,u'alphabetical-index-mark'), 
		(TEXTNS,u'bibliography-mark'), 
		(PRESENTATIONNS,u'header'), 
		(PRESENTATIONNS,u'footer'), 
		(PRESENTATIONNS,u'date-time'), 
	),
	(TEXTNS,u'alphabetical-index-auto-mark-file') : (
	),
	(TEXTNS,u'alphabetical-index-entry-template') : (
		(TEXTNS,u'index-entry-chapter'), 
		(TEXTNS,u'index-entry-page-number'), 
		(TEXTNS,u'index-entry-text'), 
		(TEXTNS,u'index-entry-span'), 
		(TEXTNS,u'index-entry-tab-stop'), 
	),
	(TEXTNS,u'alphabetical-index') : (
		(TEXTNS,u'alphabetical-index-source'), 
		(TEXTNS,u'index-body'), 
	),
	(TEXTNS,u'alphabetical-index-source') : (
		(TEXTNS,u'index-title-template'), 
		(TEXTNS,u'alphabetical-index-entry-template'), 
	),
	(TEXTNS,u'bibliography-configuration') : (
		(TEXTNS,u'sort-key'), 
	),
	(TEXTNS,u'bibliography-entry-template') : (
		(TEXTNS,u'index-entry-span'), 
		(TEXTNS,u'index-entry-tab-stop'), 
		(TEXTNS,u'index-entry-bibliography'), 
	),
	(TEXTNS,u'bibliography') : (
		(TEXTNS,u'bibliography-source'), 
		(TEXTNS,u'index-body'), 
	),
	(TEXTNS,u'bibliography-source') : (
		(TEXTNS,u'index-title-template'), 
		(TEXTNS,u'bibliography-entry-template'), 
	),
	(TEXTNS,u'bookmark-end') : (
	),
	(TEXTNS,u'bookmark') : (
	),
	(TEXTNS,u'bookmark-start') : (
	),
	(TEXTNS,u'changed-region') : (
		(TEXTNS,u'insertion'), 
		(TEXTNS,u'deletion'), 
		(TEXTNS,u'format-change'), 
	),
	(TEXTNS,u'dde-connection-decl') : (
	),
	(TEXTNS,u'h') : (
		(TEXTNS,u'number'), 
		(TEXTNS,u's'), 
		(TEXTNS,u'tab'), 
		(TEXTNS,u'line-break'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'span'), 
		(TEXTNS,u'meta'), 
		(TEXTNS,u'bookmark'), 
		(TEXTNS,u'bookmark-start'), 
		(TEXTNS,u'bookmark-end'), 
		(TEXTNS,u'reference-mark'), 
		(TEXTNS,u'reference-mark-start'), 
		(TEXTNS,u'reference-mark-end'), 
		(TEXTNS,u'note'), 
		(TEXTNS,u'ruby'), 
		(OFFICENS,u'annotation'), 
		(OFFICENS,u'annotation-end'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'date'), 
		(TEXTNS,u'time'), 
		(TEXTNS,u'page-number'), 
		(TEXTNS,u'page-continuation'), 
		(TEXTNS,u'sender-firstname'), 
		(TEXTNS,u'sender-lastname'), 
		(TEXTNS,u'sender-initials'), 
		(TEXTNS,u'sender-title'), 
		(TEXTNS,u'sender-position'), 
		(TEXTNS,u'sender-email'), 
		(TEXTNS,u'sender-phone-private'), 
		(TEXTNS,u'sender-fax'), 
		(TEXTNS,u'sender-company'), 
		(TEXTNS,u'sender-phone-work'), 
		(TEXTNS,u'sender-street'), 
		(TEXTNS,u'sender-city'), 
		(TEXTNS,u'sender-postal-code'), 
		(TEXTNS,u'sender-country'), 
		(TEXTNS,u'sender-state-or-province'), 
		(TEXTNS,u'author-name'), 
		(TEXTNS,u'author-initials'), 
		(TEXTNS,u'chapter'), 
		(TEXTNS,u'file-name'), 
		(TEXTNS,u'template-name'), 
		(TEXTNS,u'sheet-name'), 
		(TEXTNS,u'variable-set'), 
		(TEXTNS,u'variable-get'), 
		(TEXTNS,u'variable-input'), 
		(TEXTNS,u'user-field-get'), 
		(TEXTNS,u'user-field-input'), 
		(TEXTNS,u'sequence'), 
		(TEXTNS,u'expression'), 
		(TEXTNS,u'text-input'), 
		(TEXTNS,u'initial-creator'), 
		(TEXTNS,u'creation-date'), 
		(TEXTNS,u'creation-time'), 
		(TEXTNS,u'description'), 
		(TEXTNS,u'user-defined'), 
		(TEXTNS,u'print-time'), 
		(TEXTNS,u'print-date'), 
		(TEXTNS,u'printed-by'), 
		(TEXTNS,u'title'), 
		(TEXTNS,u'subject'), 
		(TEXTNS,u'keywords'), 
		(TEXTNS,u'editing-cycles'), 
		(TEXTNS,u'editing-duration'), 
		(TEXTNS,u'modification-time'), 
		(TEXTNS,u'modification-date'), 
		(TEXTNS,u'creator'), 
		(TEXTNS,u'page-count'), 
		(TEXTNS,u'paragraph-count'), 
		(TEXTNS,u'word-count'), 
		(TEXTNS,u'character-count'), 
		(TEXTNS,u'table-count'), 
		(TEXTNS,u'image-count'), 
		(TEXTNS,u'object-count'), 
		(TEXTNS,u'database-display'), 
		(TEXTNS,u'database-next'), 
		(TEXTNS,u'database-row-select'), 
		(TEXTNS,u'database-row-number'), 
		(TEXTNS,u'database-name'), 
		(TEXTNS,u'page-variable-set'), 
		(TEXTNS,u'page-variable-get'), 
		(TEXTNS,u'placeholder'), 
		(TEXTNS,u'conditional-text'), 
		(TEXTNS,u'hidden-text'), 
		(TEXTNS,u'reference-ref'), 
		(TEXTNS,u'bookmark-ref'), 
		(TEXTNS,u'note-ref'), 
		(TEXTNS,u'sequence-ref'), 
		(TEXTNS,u'script'), 
		(TEXTNS,u'execute-macro'), 
		(TEXTNS,u'hidden-paragraph'), 
		(TEXTNS,u'dde-connection'), 
		(TEXTNS,u'measure'), 
		(TEXTNS,u'table-formula'), 
		(TEXTNS,u'meta-field'), 
		(TEXTNS,u'toc-mark-start'), 
		(TEXTNS,u'toc-mark-end'), 
		(TEXTNS,u'toc-mark'), 
		(TEXTNS,u'user-index-mark-start'), 
		(TEXTNS,u'user-index-mark-end'), 
		(TEXTNS,u'user-index-mark'), 
		(TEXTNS,u'alphabetical-index-mark-start'), 
		(TEXTNS,u'alphabetical-index-mark-end'), 
		(TEXTNS,u'alphabetical-index-mark'), 
		(TEXTNS,u'bibliography-mark'), 
		(PRESENTATIONNS,u'header'), 
		(PRESENTATIONNS,u'footer'), 
		(PRESENTATIONNS,u'date-time'), 
		(TEXTNS,u'a'), 
	),
	(TEXTNS,u'illustration-index-entry-template') : (
		(TEXTNS,u'index-entry-chapter'), 
		(TEXTNS,u'index-entry-page-number'), 
		(TEXTNS,u'index-entry-text'), 
		(TEXTNS,u'index-entry-span'), 
		(TEXTNS,u'index-entry-tab-stop'), 
	),
	(TEXTNS,u'illustration-index') : (
		(TEXTNS,u'illustration-index-source'), 
		(TEXTNS,u'index-body'), 
	),
	(TEXTNS,u'illustration-index-source') : (
		(TEXTNS,u'index-title-template'), 
		(TEXTNS,u'illustration-index-entry-template'), 
	),
	(TEXTNS,u'index-body') : (
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(TEXTNS,u'index-title'), 
	),
	(TEXTNS,u'index-entry-bibliography') : (
	),
	(TEXTNS,u'index-entry-chapter') : (
	),
	(TEXTNS,u'index-entry-link-end') : (
	),
	(TEXTNS,u'index-entry-link-start') : (
	),
	(TEXTNS,u'index-entry-page-number') : (
	),
	(TEXTNS,u'index-entry-span') : (
	),
	(TEXTNS,u'index-entry-tab-stop') : (
	),
	(TEXTNS,u'index-entry-text') : (
	),
	(TEXTNS,u'index-source-style') : (
	),
	(TEXTNS,u'index-source-styles') : (
		(TEXTNS,u'index-source-style'), 
	),
	(TEXTNS,u'index-title') : (
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(TEXTNS,u'index-title'), 
	),
	(TEXTNS,u'index-title-template') : (
	),
	(TEXTNS,u'linenumbering-configuration') : (
		(TEXTNS,u'linenumbering-separator'), 
	),
	(TEXTNS,u'linenumbering-separator') : (
	),
	(TEXTNS,u'list-header') : (
		(TEXTNS,u'number'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'soft-page-break'), 
	),
	(TEXTNS,u'list') : (
		(TEXTNS,u'list-header'), 
		(TEXTNS,u'list-item'), 
	),
	(TEXTNS,u'list-item') : (
		(TEXTNS,u'number'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'soft-page-break'), 
	),
	(TEXTNS,u'list-style') : (
		(TEXTNS,u'list-level-style-number'), 
		(TEXTNS,u'list-level-style-bullet'), 
		(TEXTNS,u'list-level-style-image'), 
	),
	(TEXTNS,u'notes-configuration') : (
		(TEXTNS,u'note-continuation-notice-forward'), 
		(TEXTNS,u'note-continuation-notice-backward'), 
	),
	(TEXTNS,u'number') : (
	),
	(TEXTNS,u'numbered-paragraph') : (
		(TEXTNS,u'number'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'h'), 
	),
	(TEXTNS,u'object-index-entry-template') : (
		(TEXTNS,u'index-entry-chapter'), 
		(TEXTNS,u'index-entry-page-number'), 
		(TEXTNS,u'index-entry-text'), 
		(TEXTNS,u'index-entry-span'), 
		(TEXTNS,u'index-entry-tab-stop'), 
	),
	(TEXTNS,u'object-index') : (
		(TEXTNS,u'object-index-source'), 
		(TEXTNS,u'index-body'), 
	),
	(TEXTNS,u'object-index-source') : (
		(TEXTNS,u'index-title-template'), 
		(TEXTNS,u'object-index-entry-template'), 
	),
	(TEXTNS,u'outline-level-style') : (
		(STYLENS,u'list-level-properties'), 
		(STYLENS,u'text-properties'), 
	),
	(TEXTNS,u'outline-style') : (
		(TEXTNS,u'outline-level-style'), 
	),
	(TEXTNS,u'p') : (
		(TEXTNS,u's'), 
		(TEXTNS,u'tab'), 
		(TEXTNS,u'line-break'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'span'), 
		(TEXTNS,u'meta'), 
		(TEXTNS,u'bookmark'), 
		(TEXTNS,u'bookmark-start'), 
		(TEXTNS,u'bookmark-end'), 
		(TEXTNS,u'reference-mark'), 
		(TEXTNS,u'reference-mark-start'), 
		(TEXTNS,u'reference-mark-end'), 
		(TEXTNS,u'note'), 
		(TEXTNS,u'ruby'), 
		(OFFICENS,u'annotation'), 
		(OFFICENS,u'annotation-end'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'date'), 
		(TEXTNS,u'time'), 
		(TEXTNS,u'page-number'), 
		(TEXTNS,u'page-continuation'), 
		(TEXTNS,u'sender-firstname'), 
		(TEXTNS,u'sender-lastname'), 
		(TEXTNS,u'sender-initials'), 
		(TEXTNS,u'sender-title'), 
		(TEXTNS,u'sender-position'), 
		(TEXTNS,u'sender-email'), 
		(TEXTNS,u'sender-phone-private'), 
		(TEXTNS,u'sender-fax'), 
		(TEXTNS,u'sender-company'), 
		(TEXTNS,u'sender-phone-work'), 
		(TEXTNS,u'sender-street'), 
		(TEXTNS,u'sender-city'), 
		(TEXTNS,u'sender-postal-code'), 
		(TEXTNS,u'sender-country'), 
		(TEXTNS,u'sender-state-or-province'), 
		(TEXTNS,u'author-name'), 
		(TEXTNS,u'author-initials'), 
		(TEXTNS,u'chapter'), 
		(TEXTNS,u'file-name'), 
		(TEXTNS,u'template-name'), 
		(TEXTNS,u'sheet-name'), 
		(TEXTNS,u'variable-set'), 
		(TEXTNS,u'variable-get'), 
		(TEXTNS,u'variable-input'), 
		(TEXTNS,u'user-field-get'), 
		(TEXTNS,u'user-field-input'), 
		(TEXTNS,u'sequence'), 
		(TEXTNS,u'expression'), 
		(TEXTNS,u'text-input'), 
		(TEXTNS,u'initial-creator'), 
		(TEXTNS,u'creation-date'), 
		(TEXTNS,u'creation-time'), 
		(TEXTNS,u'description'), 
		(TEXTNS,u'user-defined'), 
		(TEXTNS,u'print-time'), 
		(TEXTNS,u'print-date'), 
		(TEXTNS,u'printed-by'), 
		(TEXTNS,u'title'), 
		(TEXTNS,u'subject'), 
		(TEXTNS,u'keywords'), 
		(TEXTNS,u'editing-cycles'), 
		(TEXTNS,u'editing-duration'), 
		(TEXTNS,u'modification-time'), 
		(TEXTNS,u'modification-date'), 
		(TEXTNS,u'creator'), 
		(TEXTNS,u'page-count'), 
		(TEXTNS,u'paragraph-count'), 
		(TEXTNS,u'word-count'), 
		(TEXTNS,u'character-count'), 
		(TEXTNS,u'table-count'), 
		(TEXTNS,u'image-count'), 
		(TEXTNS,u'object-count'), 
		(TEXTNS,u'database-display'), 
		(TEXTNS,u'database-next'), 
		(TEXTNS,u'database-row-select'), 
		(TEXTNS,u'database-row-number'), 
		(TEXTNS,u'database-name'), 
		(TEXTNS,u'page-variable-set'), 
		(TEXTNS,u'page-variable-get'), 
		(TEXTNS,u'placeholder'), 
		(TEXTNS,u'conditional-text'), 
		(TEXTNS,u'hidden-text'), 
		(TEXTNS,u'reference-ref'), 
		(TEXTNS,u'bookmark-ref'), 
		(TEXTNS,u'note-ref'), 
		(TEXTNS,u'sequence-ref'), 
		(TEXTNS,u'script'), 
		(TEXTNS,u'execute-macro'), 
		(TEXTNS,u'hidden-paragraph'), 
		(TEXTNS,u'dde-connection'), 
		(TEXTNS,u'measure'), 
		(TEXTNS,u'table-formula'), 
		(TEXTNS,u'meta-field'), 
		(TEXTNS,u'toc-mark-start'), 
		(TEXTNS,u'toc-mark-end'), 
		(TEXTNS,u'toc-mark'), 
		(TEXTNS,u'user-index-mark-start'), 
		(TEXTNS,u'user-index-mark-end'), 
		(TEXTNS,u'user-index-mark'), 
		(TEXTNS,u'alphabetical-index-mark-start'), 
		(TEXTNS,u'alphabetical-index-mark-end'), 
		(TEXTNS,u'alphabetical-index-mark'), 
		(TEXTNS,u'bibliography-mark'), 
		(PRESENTATIONNS,u'header'), 
		(PRESENTATIONNS,u'footer'), 
		(PRESENTATIONNS,u'date-time'), 
		(TEXTNS,u'a'), 
	),
	(TEXTNS,u'page') : (
	),
	(TEXTNS,u'page-sequence') : (
		(TEXTNS,u'page'), 
	),
	(TEXTNS,u'section') : (
		(TEXTNS,u'section-source'), 
		(OFFICENS,u'dde-source'), 
		(TEXTNS,u'h'), 
		(TEXTNS,u'p'), 
		(TEXTNS,u'list'), 
		(TEXTNS,u'numbered-paragraph'), 
		(TABLENS,u'table'), 
		(TEXTNS,u'section'), 
		(TEXTNS,u'soft-page-break'), 
		(TEXTNS,u'table-of-content'), 
		(TEXTNS,u'illustration-index'), 
		(TEXTNS,u'table-index'), 
		(TEXTNS,u'object-index'), 
		(TEXTNS,u'user-index'), 
		(TEXTNS,u'alphabetical-index'), 
		(TEXTNS,u'bibliography'), 
		(DRAWNS,u'rect'), 
		(DRAWNS,u'line'), 
		(DRAWNS,u'polyline'), 
		(DRAWNS,u'polygon'), 
		(DRAWNS,u'regular-polygon'), 
		(DRAWNS,u'path'), 
		(DRAWNS,u'circle'), 
		(DRAWNS,u'ellipse'), 
		(DRAWNS,u'g'), 
		(DRAWNS,u'page-thumbnail'), 
		(DRAWNS,u'frame'), 
		(DRAWNS,u'measure'), 
		(DRAWNS,u'caption'), 
		(DRAWNS,u'connector'), 
		(DRAWNS,u'control'), 
		(DR3DNS,u'scene'), 
		(DRAWNS,u'custom-shape'), 
		(DRAWNS,u'a'), 
		(TEXTNS,u'change'), 
		(TEXTNS,u'change-start'), 
		(TEXTNS,u'change-end'), 
	),
	(TEXTNS,u'section-source') : (
	),
	(TEXTNS,u'sequence-decl') : (
	),
	(TEXTNS,u'soft-page-break') : (
	),
	(TEXTNS,u'sort-key') : (
	),
	(TEXTNS,u'table-index-entry-template') : (
		(TEXTNS,u'index-entry-chapter'), 
		(TEXTNS,u'index-entry-page-number'), 
		(TEXTNS,u'index-entry-text'), 
		(TEXTNS,u'index-entry-span'), 
		(TEXTNS,u'index-entry-tab-stop'), 
	),
	(TEXTNS,u'table-index') : (
		(TEXTNS,u'table-index-source'), 
		(TEXTNS,u'index-body'), 
	),
	(TEXTNS,u'table-index-source') : (
		(TEXTNS,u'index-title-template'), 
		(TEXTNS,u'table-index-entry-template'), 
	),
	(TEXTNS,u'table-of-content-entry-template') : (
		(TEXTNS,u'index-entry-chapter'), 
		(TEXTNS,u'index-entry-page-number'), 
		(TEXTNS,u'index-entry-text'), 
		(TEXTNS,u'index-entry-span'), 
		(TEXTNS,u'index-entry-tab-stop'), 
		(TEXTNS,u'index-entry-link-start'), 
		(TEXTNS,u'index-entry-link-end'), 
	),
	(TEXTNS,u'table-of-content') : (
		(TEXTNS,u'table-of-content-source'), 
		(TEXTNS,u'index-body'), 
	),
	(TEXTNS,u'table-of-content-source') : (
		(TEXTNS,u'index-title-template'), 
		(TEXTNS,u'table-of-content-entry-template'), 
		(TEXTNS,u'index-source-styles'), 
	),
	(TEXTNS,u'user-field-decl') : (
	),
	(TEXTNS,u'user-index-entry-template') : (
		(TEXTNS,u'index-entry-chapter'), 
		(TEXTNS,u'index-entry-page-number'), 
		(TEXTNS,u'index-entry-text'), 
		(TEXTNS,u'index-entry-span'), 
		(TEXTNS,u'index-entry-tab-stop'), 
	),
	(TEXTNS,u'user-index') : (
		(TEXTNS,u'user-index-source'), 
		(TEXTNS,u'index-body'), 
	),
	(TEXTNS,u'user-index-source') : (
		(TEXTNS,u'index-title-template'), 
		(TEXTNS,u'user-index-entry-template'), 
		(TEXTNS,u'index-source-styles'), 
	),
	(TEXTNS,u'variable-decl') : (
	),
	(XFORMSNS,u'model') : 
		None,
}
allows_text = (
	(TEXTNS,u'reference-ref'),
	(TEXTNS,u'bookmark-ref'),
	(TEXTNS,u'page-count'),
	(TEXTNS,u'paragraph-count'),
	(TEXTNS,u'word-count'),
	(TEXTNS,u'character-count'),
	(TEXTNS,u'table-count'),
	(TEXTNS,u'image-count'),
	(TEXTNS,u'object-count'),
	(TEXTNS,u'author-initials'),
	(TEXTNS,u'author-name'),
	(TEXTNS,u'bibliography-mark'),
	(TEXTNS,u'chapter'),
	(TEXTNS,u'conditional-text'),
	(TEXTNS,u'creation-date'),
	(METANS,u'creation-date'),
	(TEXTNS,u'creation-time'),
	(TEXTNS,u'creator'),
	(TEXTNS,u'database-display'),
	(TEXTNS,u'database-name'),
	(TEXTNS,u'database-row-number'),
	(TEXTNS,u'date'),
	(PRESENTATIONNS,u'date-time-decl'),
	(TEXTNS,u'dde-connection'),
	(TEXTNS,u'description'),
	(DCNS,u'description'),
	(TEXTNS,u'editing-cycles'),
	(METANS,u'editing-cycles'),
	(TEXTNS,u'editing-duration'),
	(METANS,u'editing-duration'),
	(TEXTNS,u'execute-macro'),
	(TEXTNS,u'expression'),
	(TEXTNS,u'file-name'),
	(PRESENTATIONNS,u'footer-decl'),
	(METANS,u'generator'),
	(PRESENTATIONNS,u'header-decl'),
	(TEXTNS,u'hidden-paragraph'),
	(TEXTNS,u'hidden-text'),
	(TEXTNS,u'initial-creator'),
	(METANS,u'initial-creator'),
	(METANS,u'keyword'),
	(TEXTNS,u'keywords'),
	(DCNS,u'language'),
	(TEXTNS,u'measure'),
	(TEXTNS,u'meta'),
	(TEXTNS,u'meta-field'),
	(TEXTNS,u'modification-date'),
	(TEXTNS,u'modification-time'),
	(TEXTNS,u'note-citation'),
	(TEXTNS,u'note-continuation-notice-backward'),
	(TEXTNS,u'note-continuation-notice-forward'),
	(TEXTNS,u'note-ref'),
	(TEXTNS,u'page-continuation'),
	(TEXTNS,u'page-number'),
	(TEXTNS,u'page-variable-get'),
	(TEXTNS,u'page-variable-set'),
	(TEXTNS,u'placeholder'),
	(METANS,u'print-date'),
	(TEXTNS,u'print-date'),
	(TEXTNS,u'print-time'),
	(METANS,u'printed-by'),
	(TEXTNS,u'printed-by'),
	(TEXTNS,u'ruby-base'),
	(TEXTNS,u'ruby-text'),
	(TEXTNS,u'script'),
	(TEXTNS,u'sender-city'),
	(TEXTNS,u'sender-company'),
	(TEXTNS,u'sender-country'),
	(TEXTNS,u'sender-email'),
	(TEXTNS,u'sender-fax'),
	(TEXTNS,u'sender-firstname'),
	(TEXTNS,u'sender-initials'),
	(TEXTNS,u'sender-lastname'),
	(TEXTNS,u'sender-phone-private'),
	(TEXTNS,u'sender-phone-work'),
	(TEXTNS,u'sender-position'),
	(TEXTNS,u'sender-postal-code'),
	(TEXTNS,u'sender-state-or-province'),
	(TEXTNS,u'sender-street'),
	(TEXTNS,u'sender-title'),
	(TEXTNS,u'sequence'),
	(TEXTNS,u'sequence-ref'),
	(TEXTNS,u'sheet-name'),
	(TEXTNS,u'span'),
	(DCNS,u'subject'),
	(TEXTNS,u'subject'),
	(TEXTNS,u'table-formula'),
	(TEXTNS,u'template-name'),
	(TEXTNS,u'text-input'),
	(TEXTNS,u'time'),
	(DCNS,u'title'),
	(TEXTNS,u'title'),
	(TEXTNS,u'user-defined'),
	(METANS,u'user-defined'),
	(TEXTNS,u'user-field-get'),
	(TEXTNS,u'user-field-input'),
	(TEXTNS,u'variable-get'),
	(TEXTNS,u'variable-input'),
	(TEXTNS,u'variable-set'),
	(CONFIGNS,u'config-item'),
	(DBNS,u'data-source-setting-value'),
	(DBNS,u'table-filter-pattern'),
	(DBNS,u'table-type'),
	(DCNS,u'creator'),
	(DCNS,u'date'),
	(FORMNS,u'item'),
	(FORMNS,u'option'),
	(MATHNS,u'math'),
	(METANS,u'date-string'),
	(NUMBERNS,u'currency-symbol'),
	(NUMBERNS,u'embedded-text'),
	(NUMBERNS,u'text'),
	(OFFICENS,u'binary-data'),
	(OFFICENS,u'script'),
	(SVGNS,u'desc'),
	(SVGNS,u'title'),
	(TABLENS,u'desc'),
	(TABLENS,u'title'),
	(TEXTNS,u'a'),
	(TEXTNS,u'h'),
	(TEXTNS,u'index-entry-span'),
	(TEXTNS,u'index-title-template'),
	(TEXTNS,u'linenumbering-separator'),
	(TEXTNS,u'number'),
	(TEXTNS,u'p'),
)
required_attributes = {
	(ANIMNS,u'animate'): (
		(SMILNS,u'attributeName'),
	),
	(ANIMNS,u'animateColor'): (
		(SMILNS,u'attributeName'),
	),
	(ANIMNS,u'animateMotion'): (
		(SMILNS,u'attributeName'),
	),
	(ANIMNS,u'animateTransform'): (
		(SVGNS,u'type'),
		(SMILNS,u'attributeName'),
	),
	(ANIMNS,u'command'): (
		(ANIMNS,u'command'),
	),
	(ANIMNS,u'param'): (
		(ANIMNS,u'name'),
		(ANIMNS,u'value'),
	),
	(ANIMNS,u'set'): (
		(SMILNS,u'attributeName'),
	),
	(ANIMNS,u'transitionFilter'): (
		(SMILNS,u'type'),
	),
	(CHARTNS,u'axis'): (
		(CHARTNS,u'dimension'),
	),
	(CHARTNS,u'chart'): (
		(CHARTNS,u'class'),
	),
	(CHARTNS,u'error-indicator'): (
		(CHARTNS,u'dimension'),
	),
	(CHARTNS,u'symbol-image'): (
		(XLINKNS,u'href'),
	),
	(CONFIGNS,u'config-item'): (
		(CONFIGNS,u'type'),
		(CONFIGNS,u'name'),
	),
	(CONFIGNS,u'config-item-map-indexed'): (
		(CONFIGNS,u'name'),
	),
	(CONFIGNS,u'config-item-map-named'): (
		(CONFIGNS,u'name'),
	),
	(CONFIGNS,u'config-item-set'): (
		(CONFIGNS,u'name'),
	),
	(DBNS,u'column'): (
		(DBNS,u'name'),
	),
	(DBNS,u'column-definition'): (
		(DBNS,u'name'),
	),
	(DBNS,u'component'): (
		(DBNS,u'name'),
	),
	(DBNS,u'component-collection'): (
		(DBNS,u'name'),
	),
	(DBNS,u'connection-resource'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(DBNS,u'data-source-setting'): (
		(DBNS,u'data-source-setting-name'),
		(DBNS,u'data-source-setting-type'),
	),
	(DBNS,u'file-based-database'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
		(DBNS,u'media-type'),
	),
	(DBNS,u'filter-statement'): (
		(DBNS,u'command'),
	),
	(DBNS,u'index'): (
		(DBNS,u'name'),
	),
	(DBNS,u'index-column'): (
		(DBNS,u'name'),
	),
	(DBNS,u'key'): (
		(DBNS,u'type'),
	),
	(DBNS,u'order-statement'): (
		(DBNS,u'command'),
	),
	(DBNS,u'query'): (
		(DBNS,u'command'),
		(DBNS,u'name'),
	),
	(DBNS,u'query-collection'): (
		(DBNS,u'name'),
	),
	(DBNS,u'server-database'): (
		(DBNS,u'type'),
	),
	(DBNS,u'table-definition'): (
		(DBNS,u'name'),
	),
	(DBNS,u'table-representation'): (
		(DBNS,u'name'),
	),
	(DBNS,u'update-table'): (
		(DBNS,u'name'),
	),
	(NUMBERNS,u'boolean-style'): (
		(STYLENS,u'name'),
	),
	(NUMBERNS,u'currency-style'): (
		(STYLENS,u'name'),
	),
	(NUMBERNS,u'date-style'): (
		(STYLENS,u'name'),
	),
	(NUMBERNS,u'embedded-text'): (
		(NUMBERNS,u'position'),
	),
	(NUMBERNS,u'number-style'): (
		(STYLENS,u'name'),
	),
	(NUMBERNS,u'percentage-style'): (
		(STYLENS,u'name'),
	),
	(NUMBERNS,u'text-style'): (
		(STYLENS,u'name'),
	),
	(NUMBERNS,u'time-style'): (
		(STYLENS,u'name'),
	),
	(DR3DNS,u'extrude'): (
		(SVGNS,u'd'),
		(SVGNS,u'viewBox'),
	),
	(DR3DNS,u'light'): (
		(DR3DNS,u'direction'),
	),
	(DR3DNS,u'rotate'): (
		(SVGNS,u'viewBox'),
		(SVGNS,u'd'),
	),
	(DRAWNS,u'a'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(DRAWNS,u'area-circle'): (
		(SVGNS,u'cy'),
		(SVGNS,u'cx'),
		(SVGNS,u'r'),
	),
	(DRAWNS,u'area-polygon'): (
		(SVGNS,u'height'),
		(SVGNS,u'width'),
		(DRAWNS,u'points'),
		(SVGNS,u'y'),
		(SVGNS,u'x'),
		(SVGNS,u'viewBox'),
	),
	(DRAWNS,u'area-rectangle'): (
		(SVGNS,u'y'),
		(SVGNS,u'x'),
		(SVGNS,u'height'),
		(SVGNS,u'width'),
	),
	(DRAWNS,u'connector'): (
		(SVGNS,u'viewBox'),
	),
	(DRAWNS,u'contour-path'): (
		(DRAWNS,u'recreate-on-edit'),
		(SVGNS,u'viewBox'),
		(SVGNS,u'd'),
	),
	(DRAWNS,u'contour-polygon'): (
		(DRAWNS,u'points'),
		(DRAWNS,u'recreate-on-edit'),
		(SVGNS,u'viewBox'),
	),
	(DRAWNS,u'control'): (
		(DRAWNS,u'control'),
	),
	(DRAWNS,u'fill-image'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
		(DRAWNS,u'name'),
	),
	(DRAWNS,u'floating-frame'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(DRAWNS,u'glue-point'): (
		(SVGNS,u'y'),
		(SVGNS,u'x'),
		(DRAWNS,u'id'),
		(DRAWNS,u'escape-direction'),
	),
	(DRAWNS,u'gradient'): (
		(DRAWNS,u'style'),
	),
	(DRAWNS,u'handle'): (
		(DRAWNS,u'handle-position'),
	),
	(DRAWNS,u'hatch'): (
		(DRAWNS,u'style'),
		(DRAWNS,u'name'),
	),
	(DRAWNS,u'layer'): (
		(DRAWNS,u'name'),
	),
	(DRAWNS,u'line'): (
		(SVGNS,u'y1'),
		(SVGNS,u'x2'),
		(SVGNS,u'x1'),
		(SVGNS,u'y2'),
	),
	(DRAWNS,u'marker'): (
		(SVGNS,u'd'),
		(DRAWNS,u'name'),
		(SVGNS,u'viewBox'),
	),
	(DRAWNS,u'measure'): (
		(SVGNS,u'y1'),
		(SVGNS,u'x2'),
		(SVGNS,u'x1'),
		(SVGNS,u'y2'),
	),
	(DRAWNS,u'opacity'): (
		(DRAWNS,u'style'),
	),
	(DRAWNS,u'page'): (
		(DRAWNS,u'master-page-name'),
	),
	(DRAWNS,u'path'): (
		(SVGNS,u'd'),
		(SVGNS,u'viewBox'),
	),
	(DRAWNS,u'plugin'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(DRAWNS,u'polygon'): (
		(DRAWNS,u'points'),
		(SVGNS,u'viewBox'),
	),
	(DRAWNS,u'polyline'): (
		(DRAWNS,u'points'),
		(SVGNS,u'viewBox'),
	),
	(DRAWNS,u'regular-polygon'): (
		(DRAWNS,u'corners'),
	),
	(DRAWNS,u'stroke-dash'): (
		(DRAWNS,u'name'),
	),
	(FORMNS,u'connection-resource'): (
		(XLINKNS,u'href'),
	),
	(FORMNS,u'list-property'): (
		(FORMNS,u'property-name'),
	),
	(FORMNS,u'list-value'): (
		(OFFICENS,u'string-value'),
	),
	(FORMNS,u'property'): (
		(FORMNS,u'property-name'),
	),
	(MANIFESTNS,u'algorithm'): (
		(MANIFESTNS,u'initialisation-vector'),
		(MANIFESTNS,u'algorithm-name'),
	),
	(MANIFESTNS,u'encryption-data'): (
		(MANIFESTNS,u'checksum'),
		(MANIFESTNS,u'checksum-type'),
	),
	(MANIFESTNS,u'file-entry'): (
		(MANIFESTNS,u'media-type'),
		(MANIFESTNS,u'full-path'),
	),
	(MANIFESTNS,u'key-derivation'): (
		(MANIFESTNS,u'key-derivation-name'),
		(MANIFESTNS,u'iteration-count'),
		(MANIFESTNS,u'salt'),
	),
	(MANIFESTNS,u'start-key-generation'): (
		(MANIFESTNS,u'start-key-generation-name'),
	),
	(METANS,u'template'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(METANS,u'user-defined'): (
		(METANS,u'name'),
	),
	(OFFICENS,u'annotation-end'): (
		(OFFICENS,u'name'),
	),
	(OFFICENS,u'dde-source'): (
		(OFFICENS,u'dde-topic'),
		(OFFICENS,u'dde-application'),
		(OFFICENS,u'dde-item'),
	),
	(OFFICENS,u'document'): (
		(OFFICENS,u'mimetype'),
		(OFFICENS,u'version'),
	),
	(OFFICENS,u'document-content'): (
		(OFFICENS,u'version'),
	),
	(OFFICENS,u'document-meta'): (
		(OFFICENS,u'version'),
	),
	(OFFICENS,u'document-settings'): (
		(OFFICENS,u'version'),
	),
	(OFFICENS,u'document-styles'): (
		(OFFICENS,u'version'),
	),
	(OFFICENS,u'script'): (
		(SCRIPTNS,u'language'),
	),
	(PRESENTATIONNS,u'date-time-decl'): (
		(PRESENTATIONNS,u'source'),
		(PRESENTATIONNS,u'name'),
	),
	(PRESENTATIONNS,u'dim'): (
		(DRAWNS,u'color'),
		(DRAWNS,u'shape-id'),
	),
	(PRESENTATIONNS,u'event-listener'): (
		(PRESENTATIONNS,u'action'),
		(SCRIPTNS,u'event-name'),
	),
	(PRESENTATIONNS,u'footer-decl'): (
		(PRESENTATIONNS,u'name'),
	),
	(PRESENTATIONNS,u'header-decl'): (
		(PRESENTATIONNS,u'name'),
	),
	(PRESENTATIONNS,u'hide-shape'): (
		(DRAWNS,u'shape-id'),
	),
	(PRESENTATIONNS,u'hide-text'): (
		(DRAWNS,u'shape-id'),
	),
	(PRESENTATIONNS,u'placeholder'): (
		(SVGNS,u'y'),
		(SVGNS,u'x'),
		(SVGNS,u'height'),
		(PRESENTATIONNS,u'object'),
		(SVGNS,u'width'),
	),
	(PRESENTATIONNS,u'play'): (
		(DRAWNS,u'shape-id'),
	),
	(PRESENTATIONNS,u'show'): (
		(PRESENTATIONNS,u'name'),
		(PRESENTATIONNS,u'pages'),
	),
	(PRESENTATIONNS,u'show-shape'): (
		(DRAWNS,u'shape-id'),
	),
	(PRESENTATIONNS,u'show-text'): (
		(DRAWNS,u'shape-id'),
	),
	(PRESENTATIONNS,u'sound'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(SCRIPTNS,u'event-listener'): (
		(SCRIPTNS,u'language'),
		(SCRIPTNS,u'event-name'),
	),
	(STYLENS,u'column'): (
		(STYLENS,u'rel-width'),
	),
	(STYLENS,u'column-sep'): (
		(STYLENS,u'width'),
	),
	(STYLENS,u'columns'): (
		(FONS,u'column-count'),
	),
	(STYLENS,u'font-face'): (
		(STYLENS,u'name'),
	),
	(STYLENS,u'handout-master'): (
		(STYLENS,u'page-layout-name'),
	),
	(STYLENS,u'list-level-label-alignment'): (
		(TEXTNS,u'label-followed-by'),
	),
	(STYLENS,u'map'): (
		(STYLENS,u'apply-style-name'),
		(STYLENS,u'condition'),
	),
	(STYLENS,u'master-page'): (
		(STYLENS,u'page-layout-name'),
		(STYLENS,u'name'),
	),
	(STYLENS,u'page-layout'): (
		(STYLENS,u'name'),
	),
	(STYLENS,u'presentation-page-layout'): (
		(STYLENS,u'name'),
	),
	(STYLENS,u'style'): (
		(STYLENS,u'name'),
	),
	(STYLENS,u'tab-stop'): (
		(STYLENS,u'position'),
	),
	(SVGNS,u'definition-src'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(SVGNS,u'font-face-uri'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(SVGNS,u'linearGradient'): (
		(DRAWNS,u'name'),
	),
	(SVGNS,u'radialGradient'): (
		(DRAWNS,u'name'),
	),
	(SVGNS,u'stop'): (
		(SVGNS,u'offset'),
	),
	(TABLENS,u'background'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'body'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'cell-address'): (
		(TABLENS,u'column'),
		(TABLENS,u'table'),
		(TABLENS,u'row'),
	),
	(TABLENS,u'cell-content-change'): (
		(TABLENS,u'id'),
	),
	(TABLENS,u'cell-range-source'): (
		(TABLENS,u'last-row-spanned'),
		(TABLENS,u'last-column-spanned'),
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
		(TABLENS,u'name'),
	),
	(TABLENS,u'consolidation'): (
		(TABLENS,u'function'),
		(TABLENS,u'source-cell-range-addresses'),
		(TABLENS,u'target-cell-address'),
	),
	(TABLENS,u'content-validation'): (
		(TABLENS,u'name'),
	),
	(TABLENS,u'data-pilot-display-info'): (
		(TABLENS,u'member-count'),
		(TABLENS,u'data-field'),
		(TABLENS,u'enabled'),
		(TABLENS,u'display-member-mode'),
	),
	(TABLENS,u'data-pilot-field'): (
		(TABLENS,u'source-field-name'),
	),
	(TABLENS,u'data-pilot-field-reference'): (
		(TABLENS,u'field-name'),
		(TABLENS,u'type'),
	),
	(TABLENS,u'data-pilot-group'): (
		(TABLENS,u'name'),
	),
	(TABLENS,u'data-pilot-group-member'): (
		(TABLENS,u'name'),
	),
	(TABLENS,u'data-pilot-groups'): (
		(TABLENS,u'source-field-name'),
		(TABLENS,u'step'),
		(TABLENS,u'grouped-by'),
	),
	(TABLENS,u'data-pilot-layout-info'): (
		(TABLENS,u'add-empty-lines'),
		(TABLENS,u'layout-mode'),
	),
	(TABLENS,u'data-pilot-member'): (
		(TABLENS,u'name'),
	),
	(TABLENS,u'data-pilot-sort-info'): (
		(TABLENS,u'order'),
	),
	(TABLENS,u'data-pilot-subtotal'): (
		(TABLENS,u'function'),
	),
	(TABLENS,u'data-pilot-table'): (
		(TABLENS,u'target-range-address'),
		(TABLENS,u'name'),
	),
	(TABLENS,u'database-range'): (
		(TABLENS,u'target-range-address'),
	),
	(TABLENS,u'database-source-query'): (
		(TABLENS,u'query-name'),
		(TABLENS,u'database-name'),
	),
	(TABLENS,u'database-source-sql'): (
		(TABLENS,u'database-name'),
		(TABLENS,u'sql-statement'),
	),
	(TABLENS,u'database-source-table'): (
		(TABLENS,u'database-table-name'),
		(TABLENS,u'database-name'),
	),
	(TABLENS,u'deletion'): (
		(TABLENS,u'position'),
		(TABLENS,u'type'),
		(TABLENS,u'id'),
	),
	(TABLENS,u'dependency'): (
		(TABLENS,u'id'),
	),
	(TABLENS,u'even-columns'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'even-rows'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'filter-condition'): (
		(TABLENS,u'operator'),
		(TABLENS,u'field-number'),
		(TABLENS,u'value'),
	),
	(TABLENS,u'filter-set-item'): (
		(TABLENS,u'value'),
	),
	(TABLENS,u'first-column'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'first-row'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'insertion'): (
		(TABLENS,u'position'),
		(TABLENS,u'type'),
		(TABLENS,u'id'),
	),
	(TABLENS,u'insertion-cut-off'): (
		(TABLENS,u'position'),
		(TABLENS,u'id'),
	),
	(TABLENS,u'label-range'): (
		(TABLENS,u'label-cell-range-address'),
		(TABLENS,u'data-cell-range-address'),
		(TABLENS,u'orientation'),
	),
	(TABLENS,u'last-column'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'last-row'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'movement'): (
		(TABLENS,u'id'),
	),
	(TABLENS,u'named-expression'): (
		(TABLENS,u'expression'),
		(TABLENS,u'name'),
	),
	(TABLENS,u'named-range'): (
		(TABLENS,u'name'),
		(TABLENS,u'cell-range-address'),
	),
	(TABLENS,u'odd-columns'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'odd-rows'): (
		(TABLENS,u'style-name'),
	),
	(TABLENS,u'operation'): (
		(TABLENS,u'index'),
		(TABLENS,u'name'),
	),
	(TABLENS,u'scenario'): (
		(TABLENS,u'is-active'),
		(TABLENS,u'scenario-ranges'),
	),
	(TABLENS,u'sort-by'): (
		(TABLENS,u'field-number'),
	),
	(TABLENS,u'source-cell-range'): (
		(TABLENS,u'cell-range-address'),
	),
	(TABLENS,u'source-service'): (
		(TABLENS,u'source-name'),
		(TABLENS,u'object-name'),
		(TABLENS,u'name'),
	),
	(TABLENS,u'subtotal-field'): (
		(TABLENS,u'function'),
		(TABLENS,u'field-number'),
	),
	(TABLENS,u'subtotal-rule'): (
		(TABLENS,u'group-by-field-number'),
	),
	(TABLENS,u'table-source'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(TABLENS,u'table-template'): (
		(TABLENS,u'last-row-end-column'),
		(TABLENS,u'first-row-end-column'),
		(TABLENS,u'name'),
		(TABLENS,u'last-row-start-column'),
		(TABLENS,u'first-row-start-column'),
	),
	(TEXTNS,u'a'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(TEXTNS,u'alphabetical-index'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'alphabetical-index-auto-mark-file'): (
		(XLINKNS,u'href'),
		(XLINKNS,u'type'),
	),
	(TEXTNS,u'alphabetical-index-entry-template'): (
		(TEXTNS,u'style-name'),
		(TEXTNS,u'outline-level'),
	),
	(TEXTNS,u'alphabetical-index-mark'): (
		(TEXTNS,u'string-value'),
	),
	(TEXTNS,u'alphabetical-index-mark-end'): (
		(TEXTNS,u'id'),
	),
	(TEXTNS,u'alphabetical-index-mark-start'): (
		(TEXTNS,u'id'),
	),
	(TEXTNS,u'bibliography'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'bibliography-entry-template'): (
		(TEXTNS,u'style-name'),
		(TEXTNS,u'bibliography-type'),
	),
	(TEXTNS,u'bibliography-mark'): (
		(TEXTNS,u'bibliography-type'),
	),
	(TEXTNS,u'bookmark'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'bookmark-end'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'bookmark-start'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'change'): (
		(TEXTNS,u'change-id'),
	),
	(TEXTNS,u'change-end'): (
		(TEXTNS,u'change-id'),
	),
	(TEXTNS,u'change-start'): (
		(TEXTNS,u'change-id'),
	),
	(TEXTNS,u'chapter'): (
		(TEXTNS,u'display'),
		(TEXTNS,u'outline-level'),
	),
	(TEXTNS,u'conditional-text'): (
		(TEXTNS,u'string-value-if-true'),
		(TEXTNS,u'string-value-if-false'),
		(TEXTNS,u'condition'),
	),
	(TEXTNS,u'database-display'): (
		(TEXTNS,u'column-name'),
		(TEXTNS,u'table-name'),
	),
	(TEXTNS,u'database-name'): (
		(TEXTNS,u'table-name'),
	),
	(TEXTNS,u'database-next'): (
		(TEXTNS,u'table-name'),
	),
	(TEXTNS,u'database-row-number'): (
		(TEXTNS,u'table-name'),
	),
	(TEXTNS,u'database-row-select'): (
		(TEXTNS,u'table-name'),
	),
	(TEXTNS,u'dde-connection'): (
		(TEXTNS,u'connection-name'),
	),
	(TEXTNS,u'dde-connection-decl'): (
		(OFFICENS,u'dde-topic'),
		(OFFICENS,u'dde-application'),
		(OFFICENS,u'name'),
		(OFFICENS,u'dde-item'),
	),
	(TEXTNS,u'h'): (
		(TEXTNS,u'outline-level'),
	),
	(TEXTNS,u'hidden-paragraph'): (
		(TEXTNS,u'condition'),
	),
	(TEXTNS,u'hidden-text'): (
		(TEXTNS,u'string-value'),
		(TEXTNS,u'condition'),
	),
	(TEXTNS,u'illustration-index'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'illustration-index-entry-template'): (
		(TEXTNS,u'style-name'),
	),
	(TEXTNS,u'index-entry-bibliography'): (
		(TEXTNS,u'bibliography-data-field'),
	),
	(TEXTNS,u'index-source-style'): (
		(TEXTNS,u'style-name'),
	),
	(TEXTNS,u'index-source-styles'): (
		(TEXTNS,u'outline-level'),
	),
	(TEXTNS,u'index-title'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'list-level-style-bullet'): (
		(TEXTNS,u'bullet-char'),
		(TEXTNS,u'level'),
	),
	(TEXTNS,u'list-level-style-image'): (
		(TEXTNS,u'level'),
	),
	(TEXTNS,u'list-level-style-number'): (
		(TEXTNS,u'level'),
	),
	(TEXTNS,u'list-style'): (
		(STYLENS,u'name'),
	),
	(TEXTNS,u'measure'): (
		(TEXTNS,u'kind'),
	),
	(TEXTNS,u'meta-field'): (
		(XMLNS,u'id'),
	),
	(TEXTNS,u'note'): (
		(TEXTNS,u'note-class'),
	),
	(TEXTNS,u'note-ref'): (
		(TEXTNS,u'note-class'),
	),
	(TEXTNS,u'notes-configuration'): (
		(TEXTNS,u'note-class'),
	),
	(TEXTNS,u'numbered-paragraph'): (
		(TEXTNS,u'list-id'),
	),
	(TEXTNS,u'object-index'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'object-index-entry-template'): (
		(TEXTNS,u'style-name'),
	),
	(TEXTNS,u'outline-level-style'): (
		(TEXTNS,u'level'),
	),
	(TEXTNS,u'outline-style'): (
		(STYLENS,u'name'),
	),
	(TEXTNS,u'page'): (
		(TEXTNS,u'master-page-name'),
	),
	(TEXTNS,u'page-continuation'): (
		(TEXTNS,u'select-page'),
	),
	(TEXTNS,u'placeholder'): (
		(TEXTNS,u'placeholder-type'),
	),
	(TEXTNS,u'reference-mark'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'reference-mark-end'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'reference-mark-start'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'section'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'sequence'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'sequence-decl'): (
		(TEXTNS,u'display-outline-level'),
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'sort-key'): (
		(TEXTNS,u'key'),
	),
	(TEXTNS,u'table-index'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'table-index-entry-template'): (
		(TEXTNS,u'style-name'),
	),
	(TEXTNS,u'table-of-content'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'table-of-content-entry-template'): (
		(TEXTNS,u'style-name'),
		(TEXTNS,u'outline-level'),
	),
	(TEXTNS,u'toc-mark'): (
		(TEXTNS,u'string-value'),
	),
	(TEXTNS,u'toc-mark-end'): (
		(TEXTNS,u'id'),
	),
	(TEXTNS,u'toc-mark-start'): (
		(TEXTNS,u'id'),
	),
	(TEXTNS,u'user-defined'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'user-field-decl'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'user-field-get'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'user-field-input'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'user-index'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'user-index-entry-template'): (
		(TEXTNS,u'style-name'),
		(TEXTNS,u'outline-level'),
	),
	(TEXTNS,u'user-index-mark'): (
		(TEXTNS,u'index-name'),
		(TEXTNS,u'string-value'),
	),
	(TEXTNS,u'user-index-mark-end'): (
		(TEXTNS,u'id'),
	),
	(TEXTNS,u'user-index-mark-start'): (
		(TEXTNS,u'index-name'),
		(TEXTNS,u'id'),
	),
	(TEXTNS,u'user-index-source'): (
		(TEXTNS,u'index-name'),
	),
	(TEXTNS,u'variable-decl'): (
		(TEXTNS,u'name'),
		(OFFICENS,u'value-type'),
	),
	(TEXTNS,u'variable-get'): (
		(TEXTNS,u'name'),
	),
	(TEXTNS,u'variable-input'): (
		(TEXTNS,u'name'),
		(OFFICENS,u'value-type'),
	),
	(TEXTNS,u'variable-set'): (
		(TEXTNS,u'name'),
	),
}
allowed_attributes = {
# allowed_attributes
	(DCNS,u'creator'):(
	),
# allowed_attributes
	(DCNS,u'date'):(
	),
# allowed_attributes
	(DCNS,u'description'):(
	),
# allowed_attributes
	(DCNS,u'language'):(
	),
# allowed_attributes
	(DCNS,u'subject'):(
	),
# allowed_attributes
	(DCNS,u'title'):(
	),
# allowed_attributes
	(MATHNS,u'math'):(
	),
# allowed_attributes
	(XFORMSNS,u'model'):(
	),
# allowed_attributes
	(ANIMNS,u'animate'):(
		(ANIMNS,u'formula'),
		(SMILNS,u'values'),
		(SMILNS,u'dur'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'by'),
		(SMILNS,u'autoReverse'),
		(SMILNS,u'repeatCount'),
		(SMILNS,u'keyTimes'),
		(SMILNS,u'restart'),
		(SMILNS,u'restartDefault'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'repeatDur'),
		(SMILNS,u'accelerate'),
		(SMILNS,u'keySplines'),
		(SMILNS,u'attributeName'),
		(SMILNS,u'calcMode'),
		(SMILNS,u'to'),
		(SMILNS,u'additive'),
		(SMILNS,u'begin'),
		(SMILNS,u'targetElement'),
		(SMILNS,u'decelerate'),
		(SMILNS,u'accumulate'),
		(ANIMNS,u'sub-item'),
		(SMILNS,u'from'),
	),
# allowed_attributes
	(ANIMNS,u'animateColor'):(
		(ANIMNS,u'formula'),
		(SMILNS,u'values'),
		(SMILNS,u'dur'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'by'),
		(SMILNS,u'autoReverse'),
		(SMILNS,u'repeatCount'),
		(SMILNS,u'keyTimes'),
		(ANIMNS,u'color-interpolation-direction'),
		(SMILNS,u'restart'),
		(SMILNS,u'restartDefault'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'repeatDur'),
		(SMILNS,u'accelerate'),
		(SMILNS,u'from'),
		(SMILNS,u'keySplines'),
		(SMILNS,u'attributeName'),
		(SMILNS,u'calcMode'),
		(SMILNS,u'to'),
		(SMILNS,u'begin'),
		(SMILNS,u'targetElement'),
		(SMILNS,u'decelerate'),
		(SMILNS,u'accumulate'),
		(ANIMNS,u'sub-item'),
		(SMILNS,u'additive'),
		(ANIMNS,u'color-interpolation'),
	),
# allowed_attributes
	(ANIMNS,u'animateMotion'):(
		(ANIMNS,u'formula'),
		(SMILNS,u'values'),
		(SVGNS,u'origin'),
		(SMILNS,u'dur'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'by'),
		(SMILNS,u'autoReverse'),
		(SMILNS,u'repeatCount'),
		(SMILNS,u'keyTimes'),
		(SMILNS,u'restart'),
		(SMILNS,u'restartDefault'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'keySplines'),
		(SMILNS,u'accelerate'),
		(SMILNS,u'repeatDur'),
		(SMILNS,u'attributeName'),
		(SMILNS,u'calcMode'),
		(SMILNS,u'to'),
		(SMILNS,u'additive'),
		(SMILNS,u'begin'),
		(SMILNS,u'targetElement'),
		(SMILNS,u'decelerate'),
		(SMILNS,u'accumulate'),
		(ANIMNS,u'sub-item'),
		(SMILNS,u'from'),
		(SVGNS,u'path'),
	),
# allowed_attributes
	(ANIMNS,u'animateTransform'):(
		(ANIMNS,u'formula'),
		(SMILNS,u'values'),
		(SMILNS,u'dur'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'by'),
		(SMILNS,u'autoReverse'),
		(SMILNS,u'repeatCount'),
		(SVGNS,u'type'),
		(SMILNS,u'restart'),
		(SMILNS,u'restartDefault'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'accelerate'),
		(SMILNS,u'from'),
		(SMILNS,u'repeatDur'),
		(SMILNS,u'attributeName'),
		(SMILNS,u'to'),
		(SMILNS,u'begin'),
		(SMILNS,u'targetElement'),
		(SMILNS,u'decelerate'),
		(SMILNS,u'accumulate'),
		(ANIMNS,u'sub-item'),
		(SMILNS,u'additive'),
	),
# allowed_attributes
	(ANIMNS,u'audio'):(
		(PRESENTATIONNS,u'group-id'),
		(XMLNS,u'id'),
		(SMILNS,u'repeatCount'),
		(SMILNS,u'begin'),
		(SMILNS,u'restartDefault'),
		(PRESENTATIONNS,u'preset-sub-type'),
		(PRESENTATIONNS,u'node-type'),
		(PRESENTATIONNS,u'master-element'),
		(ANIMNS,u'audio-level'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'dur'),
		(SMILNS,u'restart'),
		(ANIMNS,u'id'),
		(XLINKNS,u'href'),
		(SMILNS,u'fillDefault'),
		(PRESENTATIONNS,u'preset-id'),
		(PRESENTATIONNS,u'preset-class'),
		(SMILNS,u'repeatDur'),
	),
# allowed_attributes
	(ANIMNS,u'command'):(
		(PRESENTATIONNS,u'group-id'),
		(SMILNS,u'targetElement'),
		(XMLNS,u'id'),
		(ANIMNS,u'command'),
		(PRESENTATIONNS,u'preset-sub-type'),
		(PRESENTATIONNS,u'node-type'),
		(ANIMNS,u'sub-item'),
		(PRESENTATIONNS,u'master-element'),
		(SMILNS,u'end'),
		(ANIMNS,u'id'),
		(PRESENTATIONNS,u'preset-id'),
		(PRESENTATIONNS,u'preset-class'),
		(SMILNS,u'begin'),
	),
# allowed_attributes
	(ANIMNS,u'iterate'):(
		(XMLNS,u'id'),
		(SMILNS,u'restartDefault'),
		(PRESENTATIONNS,u'node-type'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'autoReverse'),
		(SMILNS,u'repeatCount'),
		(PRESENTATIONNS,u'preset-sub-type'),
		(PRESENTATIONNS,u'master-element'),
		(SMILNS,u'restart'),
		(SMILNS,u'dur'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'endsync'),
		(SMILNS,u'accelerate'),
		(SMILNS,u'begin'),
		(SMILNS,u'repeatDur'),
		(ANIMNS,u'id'),
		(ANIMNS,u'iterate-type'),
		(PRESENTATIONNS,u'group-id'),
		(SMILNS,u'targetElement'),
		(SMILNS,u'decelerate'),
		(ANIMNS,u'sub-item'),
		(ANIMNS,u'iterate-interval'),
		(PRESENTATIONNS,u'preset-id'),
		(PRESENTATIONNS,u'preset-class'),
	),
# allowed_attributes
	(ANIMNS,u'par'):(
		(SMILNS,u'accelerate'),
		(PRESENTATIONNS,u'group-id'),
		(XMLNS,u'id'),
		(SMILNS,u'repeatCount'),
		(SMILNS,u'begin'),
		(SMILNS,u'restartDefault'),
		(PRESENTATIONNS,u'preset-sub-type'),
		(PRESENTATIONNS,u'node-type'),
		(SMILNS,u'decelerate'),
		(PRESENTATIONNS,u'master-element'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'restart'),
		(ANIMNS,u'id'),
		(SMILNS,u'dur'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'autoReverse'),
		(PRESENTATIONNS,u'preset-id'),
		(PRESENTATIONNS,u'preset-class'),
		(SMILNS,u'repeatDur'),
		(SMILNS,u'endsync'),
	),
# allowed_attributes
	(ANIMNS,u'param'):(
		(ANIMNS,u'name'),
		(ANIMNS,u'value'),
	),
# allowed_attributes
	(ANIMNS,u'seq'):(
		(SMILNS,u'accelerate'),
		(PRESENTATIONNS,u'group-id'),
		(XMLNS,u'id'),
		(SMILNS,u'repeatCount'),
		(SMILNS,u'begin'),
		(SMILNS,u'restartDefault'),
		(PRESENTATIONNS,u'preset-sub-type'),
		(PRESENTATIONNS,u'node-type'),
		(SMILNS,u'endsync'),
		(PRESENTATIONNS,u'master-element'),
		(SMILNS,u'decelerate'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'restart'),
		(ANIMNS,u'id'),
		(SMILNS,u'dur'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'autoReverse'),
		(PRESENTATIONNS,u'preset-id'),
		(PRESENTATIONNS,u'preset-class'),
		(SMILNS,u'repeatDur'),
	),
# allowed_attributes
	(ANIMNS,u'set'):(
		(SMILNS,u'accelerate'),
		(SMILNS,u'begin'),
		(SMILNS,u'targetElement'),
		(SMILNS,u'end'),
		(SMILNS,u'decelerate'),
		(SMILNS,u'dur'),
		(SMILNS,u'repeatDur'),
		(SMILNS,u'attributeName'),
		(SMILNS,u'accumulate'),
		(SMILNS,u'fill'),
		(ANIMNS,u'sub-item'),
		(SMILNS,u'to'),
		(SMILNS,u'restart'),
		(SMILNS,u'additive'),
		(SMILNS,u'restartDefault'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'autoReverse'),
		(SMILNS,u'repeatCount'),
	),
# allowed_attributes
	(ANIMNS,u'transitionFilter'):(
		(ANIMNS,u'formula'),
		(SMILNS,u'values'),
		(SMILNS,u'restartDefault'),
		(SMILNS,u'fill'),
		(SMILNS,u'end'),
		(SMILNS,u'subtype'),
		(SMILNS,u'by'),
		(SMILNS,u'autoReverse'),
		(SMILNS,u'repeatCount'),
		(SMILNS,u'mode'),
		(SMILNS,u'restart'),
		(SMILNS,u'dur'),
		(SMILNS,u'fillDefault'),
		(SMILNS,u'fadeColor'),
		(SMILNS,u'accelerate'),
		(SMILNS,u'from'),
		(SMILNS,u'begin'),
		(SMILNS,u'repeatDur'),
		(SMILNS,u'calcMode'),
		(SMILNS,u'to'),
		(SMILNS,u'type'),
		(SMILNS,u'direction'),
		(SMILNS,u'targetElement'),
		(SMILNS,u'decelerate'),
		(SMILNS,u'accumulate'),
		(ANIMNS,u'sub-item'),
		(SMILNS,u'additive'),
	),
# allowed_attributes
	(CHARTNS,u'axis'):(
		(CHARTNS,u'name'),
		(CHARTNS,u'style-name'),
		(CHARTNS,u'dimension'),
	),
# allowed_attributes
	(CHARTNS,u'categories'):(
		(TABLENS,u'cell-range-address'),
	),
# allowed_attributes
	(CHARTNS,u'chart'):(
		(XLINKNS,u'type'),
		(SVGNS,u'height'),
		(XMLNS,u'id'),
		(CHARTNS,u'column-mapping'),
		(XLINKNS,u'href'),
		(CHARTNS,u'class'),
		(SVGNS,u'width'),
		(CHARTNS,u'row-mapping'),
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'data-label'):(
		(SVGNS,u'x'),
		(SVGNS,u'y'),
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'data-point'):(
		(CHARTNS,u'style-name'),
		(CHARTNS,u'repeated'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(CHARTNS,u'domain'):(
		(TABLENS,u'cell-range-address'),
	),
# allowed_attributes
	(CHARTNS,u'equation'):(
		(CHARTNS,u'display-r-square'),
		(CHARTNS,u'style-name'),
		(CHARTNS,u'display-equation'),
		(SVGNS,u'x'),
		(SVGNS,u'y'),
		(CHARTNS,u'automatic-content'),
	),
# allowed_attributes
	(CHARTNS,u'error-indicator'):(
		(CHARTNS,u'style-name'),
		(CHARTNS,u'dimension'),
		(CHARTNS,u'error-lower-range'),
		(CHARTNS,u'error-upper-range'),
	),
# allowed_attributes
	(CHARTNS,u'floor'):(
		(SVGNS,u'width'),
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'footer'):(
		(SVGNS,u'x'),
		(TABLENS,u'cell-range'),
		(CHARTNS,u'style-name'),
		(SVGNS,u'y'),
	),
# allowed_attributes
	(CHARTNS,u'grid'):(
		(CHARTNS,u'style-name'),
		(CHARTNS,u'class'),
	),
# allowed_attributes
	(CHARTNS,u'label-separator'):(
	),
# allowed_attributes
	(CHARTNS,u'legend'):(
		(CHARTNS,u'style-name'),
		(SVGNS,u'y'),
		(STYLENS,u'legend-expansion'),
		(STYLENS,u'legend-expansion-aspect-ratio'),
		(SVGNS,u'x'),
		(CHARTNS,u'legend-position'),
		(CHARTNS,u'legend-align'),
	),
# allowed_attributes
	(CHARTNS,u'mean-value'):(
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'plot-area'):(
		(DR3DNS,u'vpn'),
		(CHARTNS,u'style-name'),
		(SVGNS,u'height'),
		(XMLNS,u'id'),
		(DR3DNS,u'vrp'),
		(DR3DNS,u'lighting-mode'),
		(DR3DNS,u'distance'),
		(DR3DNS,u'ambient-color'),
		(DR3DNS,u'vup'),
		(DR3DNS,u'shadow-slant'),
		(SVGNS,u'width'),
		(DR3DNS,u'shade-mode'),
		(DR3DNS,u'projection'),
		(DR3DNS,u'focal-length'),
		(CHARTNS,u'data-source-has-labels'),
		(SVGNS,u'x'),
		(TABLENS,u'cell-range-address'),
		(SVGNS,u'y'),
		(DR3DNS,u'transform'),
	),
# allowed_attributes
	(CHARTNS,u'regression-curve'):(
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'series'):(
		(XMLNS,u'id'),
		(CHARTNS,u'class'),
		(CHARTNS,u'values-cell-range-address'),
		(CHARTNS,u'label-cell-address'),
		(CHARTNS,u'style-name'),
		(CHARTNS,u'attached-axis'),
	),
# allowed_attributes
	(CHARTNS,u'stock-gain-marker'):(
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'stock-loss-marker'):(
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'stock-range-line'):(
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CHARTNS,u'subtitle'):(
		(SVGNS,u'x'),
		(TABLENS,u'cell-range'),
		(CHARTNS,u'style-name'),
		(SVGNS,u'y'),
	),
# allowed_attributes
	(CHARTNS,u'symbol-image'):(
		(XLINKNS,u'href'),
	),
# allowed_attributes
	(CHARTNS,u'title'):(
		(SVGNS,u'x'),
		(TABLENS,u'cell-range'),
		(CHARTNS,u'style-name'),
		(SVGNS,u'y'),
	),
# allowed_attributes
	(CHARTNS,u'wall'):(
		(SVGNS,u'width'),
		(CHARTNS,u'style-name'),
	),
# allowed_attributes
	(CONFIGNS,u'config-item'):(
		(CONFIGNS,u'name'),
		(CONFIGNS,u'type'),
	),
# allowed_attributes
	(CONFIGNS,u'config-item-map-entry'):(
		(CONFIGNS,u'name'),
	),
# allowed_attributes
	(CONFIGNS,u'config-item-map-indexed'):(
		(CONFIGNS,u'name'),
	),
# allowed_attributes
	(CONFIGNS,u'config-item-map-named'):(
		(CONFIGNS,u'name'),
	),
# allowed_attributes
	(CONFIGNS,u'config-item-set'):(
		(CONFIGNS,u'name'),
	),
# allowed_attributes
	(DBNS,u'application-connection-settings'):(
		(DBNS,u'suppress-version-columns'),
		(DBNS,u'boolean-comparison-mode'),
		(DBNS,u'max-row-count'),
		(DBNS,u'is-table-name-length-limited'),
		(DBNS,u'use-catalog'),
		(DBNS,u'enable-sql92-check'),
		(DBNS,u'append-table-alias-name'),
		(DBNS,u'ignore-driver-privileges'),
	),
# allowed_attributes
	(DBNS,u'auto-increment'):(
		(DBNS,u'row-retrieving-statement'),
		(DBNS,u'additional-column-statement'),
	),
# allowed_attributes
	(DBNS,u'character-set'):(
		(DBNS,u'encoding'),
	),
# allowed_attributes
	(DBNS,u'column'):(
		(DBNS,u'default-cell-style-name'),
		(OFFICENS,u'value'),
		(OFFICENS,u'value-type'),
		(DBNS,u'name'),
		(OFFICENS,u'date-value'),
		(DBNS,u'visible'),
		(DBNS,u'title'),
		(OFFICENS,u'currency'),
		(DBNS,u'style-name'),
		(OFFICENS,u'string-value'),
		(OFFICENS,u'boolean-value'),
		(DBNS,u'description'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(DBNS,u'column-definition'):(
		(DBNS,u'precision'),
		(DBNS,u'scale'),
		(OFFICENS,u'value'),
		(OFFICENS,u'value-type'),
		(DBNS,u'name'),
		(DBNS,u'type-name'),
		(DBNS,u'is-empty-allowed'),
		(OFFICENS,u'currency'),
		(OFFICENS,u'date-value'),
		(OFFICENS,u'string-value'),
		(DBNS,u'is-nullable'),
		(OFFICENS,u'boolean-value'),
		(DBNS,u'is-autoincrement'),
		(DBNS,u'data-type'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(DBNS,u'column-definitions'):(
	),
# allowed_attributes
	(DBNS,u'columns'):(
	),
# allowed_attributes
	(DBNS,u'component'):(
		(XLINKNS,u'type'),
		(DBNS,u'title'),
		(XLINKNS,u'show'),
		(XLINKNS,u'href'),
		(DBNS,u'name'),
		(XLINKNS,u'actuate'),
		(DBNS,u'as-template'),
		(DBNS,u'description'),
	),
# allowed_attributes
	(DBNS,u'component-collection'):(
		(DBNS,u'title'),
		(DBNS,u'name'),
		(DBNS,u'description'),
	),
# allowed_attributes
	(DBNS,u'connection-data'):(
	),
# allowed_attributes
	(DBNS,u'connection-resource'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(DBNS,u'data-source'):(
	),
# allowed_attributes
	(DBNS,u'data-source-setting'):(
		(DBNS,u'data-source-setting-type'),
		(DBNS,u'data-source-setting-name'),
		(DBNS,u'data-source-setting-is-list'),
	),
# allowed_attributes
	(DBNS,u'data-source-setting-value'):(
	),
# allowed_attributes
	(DBNS,u'data-source-settings'):(
	),
# allowed_attributes
	(DBNS,u'database-description'):(
	),
# allowed_attributes
	(DBNS,u'delimiter'):(
		(DBNS,u'string'),
		(DBNS,u'thousand'),
		(DBNS,u'field'),
		(DBNS,u'decimal'),
	),
# allowed_attributes
	(DBNS,u'driver-settings'):(
		(DBNS,u'show-deleted'),
		(DBNS,u'parameter-name-substitution'),
		(DBNS,u'base-dn'),
		(DBNS,u'system-driver-settings'),
		(DBNS,u'is-first-row-header-line'),
	),
# allowed_attributes
	(DBNS,u'file-based-database'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(DBNS,u'extension'),
		(DBNS,u'media-type'),
	),
# allowed_attributes
	(DBNS,u'filter-statement'):(
		(DBNS,u'apply-command'),
		(DBNS,u'command'),
	),
# allowed_attributes
	(DBNS,u'forms'):(
	),
# allowed_attributes
	(DBNS,u'index'):(
		(DBNS,u'name'),
		(DBNS,u'is-clustered'),
		(DBNS,u'catalog-name'),
		(DBNS,u'is-unique'),
	),
# allowed_attributes
	(DBNS,u'index-column'):(
		(DBNS,u'name'),
		(DBNS,u'is-ascending'),
	),
# allowed_attributes
	(DBNS,u'index-columns'):(
	),
# allowed_attributes
	(DBNS,u'indices'):(
	),
# allowed_attributes
	(DBNS,u'key'):(
		(DBNS,u'delete-rule'),
		(DBNS,u'name'),
		(DBNS,u'referenced-table-name'),
		(DBNS,u'type'),
		(DBNS,u'update-rule'),
	),
# allowed_attributes
	(DBNS,u'key-column'):(
		(DBNS,u'related-column-name'),
		(DBNS,u'name'),
	),
# allowed_attributes
	(DBNS,u'key-columns'):(
	),
# allowed_attributes
	(DBNS,u'keys'):(
	),
# allowed_attributes
	(DBNS,u'login'):(
		(DBNS,u'use-system-user'),
		(DBNS,u'is-password-required'),
		(DBNS,u'login-timeout'),
		(DBNS,u'user-name'),
	),
# allowed_attributes
	(DBNS,u'order-statement'):(
		(DBNS,u'apply-command'),
		(DBNS,u'command'),
	),
# allowed_attributes
	(DBNS,u'queries'):(
	),
# allowed_attributes
	(DBNS,u'query'):(
		(DBNS,u'name'),
		(DBNS,u'default-row-style-name'),
		(DBNS,u'command'),
		(DBNS,u'title'),
		(DBNS,u'style-name'),
		(DBNS,u'description'),
		(DBNS,u'escape-processing'),
	),
# allowed_attributes
	(DBNS,u'query-collection'):(
		(DBNS,u'title'),
		(DBNS,u'name'),
		(DBNS,u'description'),
	),
# allowed_attributes
	(DBNS,u'reports'):(
	),
# allowed_attributes
	(DBNS,u'schema-definition'):(
	),
# allowed_attributes
	(DBNS,u'server-database'):(
		(DBNS,u'database-name'),
		(DBNS,u'port'),
		(DBNS,u'hostname'),
		(DBNS,u'type'),
		(DBNS,u'local-socket'),
	),
# allowed_attributes
	(DBNS,u'table-definition'):(
		(DBNS,u'schema-name'),
		(DBNS,u'name'),
		(DBNS,u'catalog-name'),
		(DBNS,u'type'),
	),
# allowed_attributes
	(DBNS,u'table-definitions'):(
	),
# allowed_attributes
	(DBNS,u'table-exclude-filter'):(
	),
# allowed_attributes
	(DBNS,u'table-filter'):(
	),
# allowed_attributes
	(DBNS,u'table-filter-pattern'):(
	),
# allowed_attributes
	(DBNS,u'table-include-filter'):(
	),
# allowed_attributes
	(DBNS,u'table-representation'):(
		(DBNS,u'schema-name'),
		(DBNS,u'name'),
		(DBNS,u'default-row-style-name'),
		(DBNS,u'title'),
		(DBNS,u'style-name'),
		(DBNS,u'catalog-name'),
		(DBNS,u'description'),
	),
# allowed_attributes
	(DBNS,u'table-representations'):(
	),
# allowed_attributes
	(DBNS,u'table-setting'):(
		(DBNS,u'show-deleted'),
		(DBNS,u'is-first-row-header-line'),
	),
# allowed_attributes
	(DBNS,u'table-settings'):(
	),
# allowed_attributes
	(DBNS,u'table-type'):(
	),
# allowed_attributes
	(DBNS,u'table-type-filter'):(
	),
# allowed_attributes
	(DBNS,u'update-table'):(
		(DBNS,u'schema-name'),
		(DBNS,u'name'),
		(DBNS,u'catalog-name'),
	),
# allowed_attributes
	(NUMBERNS,u'am-pm'):(
	),
# allowed_attributes
	(NUMBERNS,u'boolean'):(
	),
# allowed_attributes
	(NUMBERNS,u'boolean-style'):(
		(NUMBERNS,u'country'),
		(NUMBERNS,u'transliteration-style'),
		(NUMBERNS,u'language'),
		(STYLENS,u'volatile'),
		(NUMBERNS,u'script'),
		(NUMBERNS,u'rfc-language-tag'),
		(NUMBERNS,u'transliteration-language'),
		(NUMBERNS,u'title'),
		(STYLENS,u'name'),
		(NUMBERNS,u'transliteration-format'),
		(NUMBERNS,u'transliteration-country'),
	),
# allowed_attributes
	(NUMBERNS,u'currency-style'):(
		(NUMBERNS,u'country'),
		(NUMBERNS,u'transliteration-style'),
		(NUMBERNS,u'language'),
		(STYLENS,u'volatile'),
		(NUMBERNS,u'script'),
		(NUMBERNS,u'rfc-language-tag'),
		(NUMBERNS,u'automatic-order'),
		(NUMBERNS,u'transliteration-language'),
		(NUMBERNS,u'title'),
		(STYLENS,u'name'),
		(NUMBERNS,u'transliteration-format'),
		(NUMBERNS,u'transliteration-country'),
	),
# allowed_attributes
	(NUMBERNS,u'currency-symbol'):(
		(NUMBERNS,u'script'),
		(NUMBERNS,u'country'),
		(NUMBERNS,u'language'),
		(NUMBERNS,u'rfc-language-tag'),
	),
# allowed_attributes
	(NUMBERNS,u'date-style'):(
		(NUMBERNS,u'country'),
		(NUMBERNS,u'transliteration-style'),
		(NUMBERNS,u'language'),
		(STYLENS,u'volatile'),
		(NUMBERNS,u'script'),
		(NUMBERNS,u'rfc-language-tag'),
		(NUMBERNS,u'automatic-order'),
		(NUMBERNS,u'format-source'),
		(NUMBERNS,u'transliteration-language'),
		(NUMBERNS,u'title'),
		(STYLENS,u'name'),
		(NUMBERNS,u'transliteration-format'),
		(NUMBERNS,u'transliteration-country'),
	),
# allowed_attributes
	(NUMBERNS,u'day'):(
		(NUMBERNS,u'style'),
		(NUMBERNS,u'calendar'),
	),
# allowed_attributes
	(NUMBERNS,u'day-of-week'):(
		(NUMBERNS,u'style'),
		(NUMBERNS,u'calendar'),
	),
# allowed_attributes
	(NUMBERNS,u'embedded-text'):(
		(NUMBERNS,u'position'),
	),
# allowed_attributes
	(NUMBERNS,u'era'):(
		(NUMBERNS,u'style'),
		(NUMBERNS,u'calendar'),
	),
# allowed_attributes
	(NUMBERNS,u'fraction'):(
		(NUMBERNS,u'grouping'),
		(NUMBERNS,u'denominator-value'),
		(NUMBERNS,u'min-denominator-digits'),
		(NUMBERNS,u'min-integer-digits'),
		(NUMBERNS,u'min-numerator-digits'),
	),
# allowed_attributes
	(NUMBERNS,u'hours'):(
		(NUMBERNS,u'style'),
	),
# allowed_attributes
	(NUMBERNS,u'minutes'):(
		(NUMBERNS,u'style'),
	),
# allowed_attributes
	(NUMBERNS,u'month'):(
		(NUMBERNS,u'style'),
		(NUMBERNS,u'calendar'),
		(NUMBERNS,u'possessive-form'),
		(NUMBERNS,u'textual'),
	),
# allowed_attributes
	(NUMBERNS,u'number'):(
		(NUMBERNS,u'display-factor'),
		(NUMBERNS,u'grouping'),
		(NUMBERNS,u'decimal-places'),
		(NUMBERNS,u'min-integer-digits'),
		(NUMBERNS,u'decimal-replacement'),
	),
# allowed_attributes
	(NUMBERNS,u'number-style'):(
		(NUMBERNS,u'country'),
		(NUMBERNS,u'transliteration-style'),
		(NUMBERNS,u'language'),
		(STYLENS,u'volatile'),
		(NUMBERNS,u'script'),
		(NUMBERNS,u'rfc-language-tag'),
		(NUMBERNS,u'transliteration-language'),
		(NUMBERNS,u'title'),
		(STYLENS,u'name'),
		(NUMBERNS,u'transliteration-format'),
		(NUMBERNS,u'transliteration-country'),
	),
# allowed_attributes
	(NUMBERNS,u'percentage-style'):(
		(NUMBERNS,u'country'),
		(NUMBERNS,u'transliteration-style'),
		(NUMBERNS,u'language'),
		(STYLENS,u'volatile'),
		(NUMBERNS,u'script'),
		(NUMBERNS,u'rfc-language-tag'),
		(NUMBERNS,u'transliteration-language'),
		(NUMBERNS,u'title'),
		(STYLENS,u'name'),
		(NUMBERNS,u'transliteration-format'),
		(NUMBERNS,u'transliteration-country'),
	),
# allowed_attributes
	(NUMBERNS,u'quarter'):(
		(NUMBERNS,u'style'),
		(NUMBERNS,u'calendar'),
	),
# allowed_attributes
	(NUMBERNS,u'scientific-number'):(
		(NUMBERNS,u'min-exponent-digits'),
		(NUMBERNS,u'grouping'),
		(NUMBERNS,u'decimal-places'),
		(NUMBERNS,u'min-integer-digits'),
	),
# allowed_attributes
	(NUMBERNS,u'seconds'):(
		(NUMBERNS,u'style'),
		(NUMBERNS,u'decimal-places'),
	),
# allowed_attributes
	(NUMBERNS,u'text'):(
	),
# allowed_attributes
	(NUMBERNS,u'text-content'):(
	),
# allowed_attributes
	(NUMBERNS,u'text-style'):(
		(NUMBERNS,u'country'),
		(NUMBERNS,u'transliteration-style'),
		(NUMBERNS,u'language'),
		(STYLENS,u'volatile'),
		(NUMBERNS,u'script'),
		(NUMBERNS,u'rfc-language-tag'),
		(NUMBERNS,u'transliteration-language'),
		(NUMBERNS,u'title'),
		(STYLENS,u'name'),
		(NUMBERNS,u'transliteration-format'),
		(NUMBERNS,u'transliteration-country'),
	),
# allowed_attributes
	(NUMBERNS,u'time-style'):(
		(NUMBERNS,u'country'),
		(NUMBERNS,u'transliteration-style'),
		(NUMBERNS,u'language'),
		(STYLENS,u'volatile'),
		(NUMBERNS,u'script'),
		(NUMBERNS,u'transliteration-format'),
		(NUMBERNS,u'format-source'),
		(NUMBERNS,u'transliteration-language'),
		(NUMBERNS,u'rfc-language-tag'),
		(NUMBERNS,u'title'),
		(STYLENS,u'name'),
		(NUMBERNS,u'truncate-on-overflow'),
		(NUMBERNS,u'transliteration-country'),
	),
# allowed_attributes
	(NUMBERNS,u'week-of-year'):(
		(NUMBERNS,u'calendar'),
	),
# allowed_attributes
	(NUMBERNS,u'year'):(
		(NUMBERNS,u'style'),
		(NUMBERNS,u'calendar'),
	),
# allowed_attributes
	(DR3DNS,u'cube'):(
		(DRAWNS,u'style-name'),
		(PRESENTATIONNS,u'style-name'),
		(DRAWNS,u'id'),
		(XMLNS,u'id'),
		(DR3DNS,u'min-edge'),
		(DR3DNS,u'max-edge'),
		(PRESENTATIONNS,u'class-names'),
		(DRAWNS,u'layer'),
		(DRAWNS,u'class-names'),
		(DR3DNS,u'transform'),
		(DRAWNS,u'z-index'),
	),
# allowed_attributes
	(DR3DNS,u'extrude'):(
		(DRAWNS,u'style-name'),
		(PRESENTATIONNS,u'style-name'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'layer'),
		(SVGNS,u'd'),
		(DRAWNS,u'class-names'),
		(DR3DNS,u'transform'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(DR3DNS,u'light'):(
		(DR3DNS,u'specular'),
		(DR3DNS,u'enabled'),
		(DR3DNS,u'diffuse-color'),
		(DR3DNS,u'direction'),
	),
# allowed_attributes
	(DR3DNS,u'rotate'):(
		(DRAWNS,u'style-name'),
		(PRESENTATIONNS,u'style-name'),
		(DRAWNS,u'id'),
		(XMLNS,u'id'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'layer'),
		(SVGNS,u'd'),
		(DRAWNS,u'class-names'),
		(DR3DNS,u'transform'),
		(DRAWNS,u'z-index'),
	),
# allowed_attributes
	(DR3DNS,u'scene'):(
		(DR3DNS,u'distance'),
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DR3DNS,u'shadow-slant'),
		(DR3DNS,u'lighting-mode'),
		(DRAWNS,u'layer'),
		(DR3DNS,u'projection'),
		(SVGNS,u'x'),
		(DR3DNS,u'transform'),
		(TEXTNS,u'anchor-page-number'),
		(DR3DNS,u'ambient-color'),
		(DRAWNS,u'z-index'),
		(DR3DNS,u'vrp'),
		(DR3DNS,u'shade-mode'),
		(DR3DNS,u'focal-length'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DR3DNS,u'vpn'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(DR3DNS,u'vup'),
		(DRAWNS,u'id'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DR3DNS,u'sphere'):(
		(DRAWNS,u'style-name'),
		(PRESENTATIONNS,u'style-name'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(PRESENTATIONNS,u'class-names'),
		(DR3DNS,u'size'),
		(DRAWNS,u'layer'),
		(DR3DNS,u'center'),
		(DRAWNS,u'class-names'),
		(DR3DNS,u'transform'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(DRAWNS,u'a'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'show'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(OFFICENS,u'title'),
		(OFFICENS,u'server-map'),
		(OFFICENS,u'name'),
		(OFFICENS,u'target-frame-name'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(DRAWNS,u'applet'):(
		(XLINKNS,u'type'),
		(DRAWNS,u'archive'),
		(XMLNS,u'id'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(DRAWNS,u'code'),
		(DRAWNS,u'object'),
		(DRAWNS,u'may-script'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(DRAWNS,u'area-circle'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'show'),
		(XLINKNS,u'href'),
		(DRAWNS,u'nohref'),
		(SVGNS,u'r'),
		(OFFICENS,u'name'),
		(SVGNS,u'cx'),
		(SVGNS,u'cy'),
		(OFFICENS,u'target-frame-name'),
	),
# allowed_attributes
	(DRAWNS,u'area-polygon'):(
		(XLINKNS,u'type'),
		(DRAWNS,u'points'),
		(SVGNS,u'height'),
		(XLINKNS,u'show'),
		(XLINKNS,u'href'),
		(DRAWNS,u'nohref'),
		(SVGNS,u'viewBox'),
		(SVGNS,u'width'),
		(OFFICENS,u'name'),
		(SVGNS,u'x'),
		(OFFICENS,u'target-frame-name'),
		(SVGNS,u'y'),
	),
# allowed_attributes
	(DRAWNS,u'area-rectangle'):(
		(XLINKNS,u'type'),
		(SVGNS,u'height'),
		(XLINKNS,u'show'),
		(XLINKNS,u'href'),
		(DRAWNS,u'nohref'),
		(SVGNS,u'width'),
		(OFFICENS,u'name'),
		(SVGNS,u'x'),
		(OFFICENS,u'target-frame-name'),
		(SVGNS,u'y'),
	),
# allowed_attributes
	(DRAWNS,u'caption'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(DRAWNS,u'caption-point-y'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'corner-radius'),
		(DRAWNS,u'transform'),
		(DRAWNS,u'caption-point-x'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'circle'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'cx'),
		(SVGNS,u'x'),
		(DRAWNS,u'end-angle'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(DRAWNS,u'kind'),
		(DRAWNS,u'start-angle'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(TABLENS,u'end-y'),
		(DRAWNS,u'text-style-name'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(SVGNS,u'r'),
		(TABLENS,u'end-cell-address'),
		(SVGNS,u'cy'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'connector'):(
		(SVGNS,u'y2'),
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'end-shape'),
		(DRAWNS,u'name'),
		(DRAWNS,u'caption-id'),
		(DRAWNS,u'layer'),
		(SVGNS,u'y1'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'transform'),
		(DRAWNS,u'start-glue-point'),
		(TABLENS,u'table-background'),
		(DRAWNS,u'start-shape'),
		(DRAWNS,u'end-glue-point'),
		(SVGNS,u'x1'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'x2'),
		(DRAWNS,u'type'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(DRAWNS,u'line-skew'),
		(TEXTNS,u'anchor-type'),
		(SVGNS,u'd'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'contour-path'):(
		(SVGNS,u'width'),
		(SVGNS,u'height'),
		(SVGNS,u'd'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'recreate-on-edit'),
	),
# allowed_attributes
	(DRAWNS,u'contour-polygon'):(
		(SVGNS,u'width'),
		(SVGNS,u'height'),
		(DRAWNS,u'points'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'recreate-on-edit'),
	),
# allowed_attributes
	(DRAWNS,u'control'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(DRAWNS,u'control'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'class-names'),
		(SVGNS,u'y'),
		(DRAWNS,u'text-style-name'),
	),
# allowed_attributes
	(DRAWNS,u'custom-shape'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(DRAWNS,u'engine'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(DRAWNS,u'data'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'ellipse'):(
		(SVGNS,u'rx'),
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'cx'),
		(SVGNS,u'x'),
		(DRAWNS,u'end-angle'),
		(SVGNS,u'ry'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(DRAWNS,u'kind'),
		(DRAWNS,u'start-angle'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(TABLENS,u'end-y'),
		(DRAWNS,u'text-style-name'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(SVGNS,u'cy'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'enhanced-geometry'):(
		(DRAWNS,u'extrusion-light-face'),
		(DRAWNS,u'glue-point-leaving-directions'),
		(DRAWNS,u'text-path-mode'),
		(DRAWNS,u'extrusion-rotation-angle'),
		(DRAWNS,u'text-rotate-angle'),
		(DRAWNS,u'extrusion-first-light-direction'),
		(DR3DNS,u'projection'),
		(DRAWNS,u'extrusion-skew'),
		(DRAWNS,u'extrusion-color'),
		(DRAWNS,u'text-path-allowed'),
		(DRAWNS,u'concentric-gradient-fill-allowed'),
		(DRAWNS,u'mirror-horizontal'),
		(DRAWNS,u'extrusion-depth'),
		(DRAWNS,u'extrusion-allowed'),
		(DRAWNS,u'glue-point-type'),
		(DRAWNS,u'extrusion-second-light-level'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'glue-points'),
		(DRAWNS,u'extrusion-rotation-center'),
		(DR3DNS,u'shade-mode'),
		(DRAWNS,u'text-path-scale'),
		(DRAWNS,u'extrusion-metal'),
		(DRAWNS,u'text-path-same-letter-heights'),
		(DRAWNS,u'path-stretchpoint-y'),
		(DRAWNS,u'path-stretchpoint-x'),
		(DRAWNS,u'mirror-vertical'),
		(DRAWNS,u'modifiers'),
		(DRAWNS,u'extrusion-diffusion'),
		(DRAWNS,u'text-areas'),
		(DRAWNS,u'extrusion-first-light-level'),
		(DRAWNS,u'text-path'),
		(DRAWNS,u'type'),
		(DRAWNS,u'extrusion-shininess'),
		(DRAWNS,u'extrusion-second-light-harsh'),
		(DRAWNS,u'enhanced-path'),
		(DRAWNS,u'extrusion'),
		(DRAWNS,u'extrusion-second-light-direction'),
		(DRAWNS,u'extrusion-viewpoint'),
		(DRAWNS,u'extrusion-brightness'),
		(DRAWNS,u'extrusion-origin'),
		(DRAWNS,u'extrusion-number-of-line-segments'),
		(DRAWNS,u'extrusion-first-light-harsh'),
		(DRAWNS,u'extrusion-specularity'),
	),
# allowed_attributes
	(DRAWNS,u'equation'):(
		(DRAWNS,u'formula'),
		(DRAWNS,u'name'),
	),
# allowed_attributes
	(DRAWNS,u'fill-image'):(
		(XLINKNS,u'type'),
		(SVGNS,u'height'),
		(XLINKNS,u'show'),
		(XLINKNS,u'href'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(XLINKNS,u'actuate'),
		(SVGNS,u'width'),
	),
# allowed_attributes
	(DRAWNS,u'floating-frame'):(
		(XLINKNS,u'type'),
		(XMLNS,u'id'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(DRAWNS,u'frame-name'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(DRAWNS,u'frame'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'copy-of'),
		(DRAWNS,u'name'),
		(PRESENTATIONNS,u'user-transformed'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(PRESENTATIONNS,u'class'),
		(STYLENS,u'rel-height'),
		(STYLENS,u'rel-width'),
		(PRESENTATIONNS,u'placeholder'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'class-names'),
		(SVGNS,u'y'),
		(DRAWNS,u'text-style-name'),
	),
# allowed_attributes
	(DRAWNS,u'g'):(
		(DRAWNS,u'style-name'),
		(PRESENTATIONNS,u'style-name'),
		(DRAWNS,u'id'),
		(XMLNS,u'id'),
		(TABLENS,u'end-y'),
		(DRAWNS,u'name'),
		(TEXTNS,u'anchor-page-number'),
		(PRESENTATIONNS,u'class-names'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-x'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'class-names'),
		(TABLENS,u'table-background'),
		(SVGNS,u'y'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'z-index'),
	),
# allowed_attributes
	(DRAWNS,u'glue-point'):(
		(DRAWNS,u'escape-direction'),
		(SVGNS,u'x'),
		(DRAWNS,u'id'),
		(SVGNS,u'y'),
		(DRAWNS,u'align'),
	),
# allowed_attributes
	(DRAWNS,u'gradient'):(
		(DRAWNS,u'end-intensity'),
		(DRAWNS,u'cx'),
		(DRAWNS,u'cy'),
		(DRAWNS,u'border'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(DRAWNS,u'angle'),
		(DRAWNS,u'start-color'),
		(DRAWNS,u'style'),
		(DRAWNS,u'end-color'),
		(DRAWNS,u'start-intensity'),
	),
# allowed_attributes
	(DRAWNS,u'handle'):(
		(DRAWNS,u'handle-range-y-maximum'),
		(DRAWNS,u'handle-position'),
		(DRAWNS,u'handle-range-x-maximum'),
		(DRAWNS,u'handle-range-x-minimum'),
		(DRAWNS,u'handle-polar'),
		(DRAWNS,u'handle-switched'),
		(DRAWNS,u'handle-mirror-horizontal'),
		(DRAWNS,u'handle-mirror-vertical'),
		(DRAWNS,u'handle-radius-range-maximum'),
		(DRAWNS,u'handle-radius-range-minimum'),
		(DRAWNS,u'handle-range-y-minimum'),
	),
# allowed_attributes
	(DRAWNS,u'hatch'):(
		(DRAWNS,u'color'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(DRAWNS,u'rotation'),
		(DRAWNS,u'style'),
		(DRAWNS,u'distance'),
	),
# allowed_attributes
	(DRAWNS,u'image'):(
		(XLINKNS,u'type'),
		(XMLNS,u'id'),
		(DRAWNS,u'filter-name'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(DRAWNS,u'image-map'):(
	),
# allowed_attributes
	(DRAWNS,u'layer'):(
		(DRAWNS,u'display'),
		(DRAWNS,u'protected'),
		(DRAWNS,u'name'),
	),
# allowed_attributes
	(DRAWNS,u'layer-set'):(
	),
# allowed_attributes
	(DRAWNS,u'line'):(
		(SVGNS,u'y2'),
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'y1'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(SVGNS,u'x1'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'x2'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'class-names'),
		(DRAWNS,u'text-style-name'),
	),
# allowed_attributes
	(DRAWNS,u'marker'):(
		(SVGNS,u'd'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(SVGNS,u'viewBox'),
	),
# allowed_attributes
	(DRAWNS,u'measure'):(
		(SVGNS,u'y2'),
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'y1'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(SVGNS,u'x1'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'x2'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'class-names'),
		(DRAWNS,u'text-style-name'),
	),
# allowed_attributes
	(DRAWNS,u'object'):(
		(XLINKNS,u'type'),
		(XMLNS,u'id'),
		(DRAWNS,u'notify-on-update-of-ranges'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(DRAWNS,u'object-ole'):(
		(XLINKNS,u'type'),
		(DRAWNS,u'class-id'),
		(XMLNS,u'id'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(DRAWNS,u'opacity'):(
		(DRAWNS,u'cx'),
		(DRAWNS,u'cy'),
		(DRAWNS,u'border'),
		(DRAWNS,u'start'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(DRAWNS,u'angle'),
		(DRAWNS,u'style'),
		(DRAWNS,u'end'),
	),
# allowed_attributes
	(DRAWNS,u'page'):(
		(DRAWNS,u'nav-order'),
		(DRAWNS,u'style-name'),
		(DRAWNS,u'id'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(PRESENTATIONNS,u'presentation-page-layout-name'),
		(PRESENTATIONNS,u'use-date-time-name'),
		(DRAWNS,u'master-page-name'),
		(PRESENTATIONNS,u'use-header-name'),
		(PRESENTATIONNS,u'use-footer-name'),
	),
# allowed_attributes
	(DRAWNS,u'page-thumbnail'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(PRESENTATIONNS,u'user-transformed'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(PRESENTATIONNS,u'class'),
		(DRAWNS,u'page-number'),
		(PRESENTATIONNS,u'placeholder'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'param'):(
		(DRAWNS,u'value'),
		(DRAWNS,u'name'),
	),
# allowed_attributes
	(DRAWNS,u'path'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(SVGNS,u'd'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'plugin'):(
		(XLINKNS,u'type'),
		(XMLNS,u'id'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(DRAWNS,u'mime-type'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(DRAWNS,u'polygon'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(DRAWNS,u'points'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(TEXTNS,u'anchor-page-number'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'polyline'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(DRAWNS,u'points'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(SVGNS,u'viewBox'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(TEXTNS,u'anchor-page-number'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'rect'):(
		(SVGNS,u'rx'),
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(SVGNS,u'ry'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'corner-radius'),
		(DRAWNS,u'transform'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'regular-polygon'):(
		(DRAWNS,u'corners'),
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'transform'),
		(DRAWNS,u'sharpness'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(DRAWNS,u'concave'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(DRAWNS,u'caption-id'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(DRAWNS,u'stroke-dash'):(
		(DRAWNS,u'dots2'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(DRAWNS,u'dots1'),
		(DRAWNS,u'dots1-length'),
		(DRAWNS,u'distance'),
		(DRAWNS,u'dots2-length'),
		(DRAWNS,u'style'),
	),
# allowed_attributes
	(DRAWNS,u'text-box'):(
		(FONS,u'max-height'),
		(FONS,u'min-width'),
		(TEXTNS,u'id'),
		(XMLNS,u'id'),
		(DRAWNS,u'corner-radius'),
		(DRAWNS,u'chain-next-name'),
		(FONS,u'max-width'),
		(FONS,u'min-height'),
	),
# allowed_attributes
	(FORMNS,u'button'):(
		(XMLNS,u'id'),
		(FORMNS,u'image-data'),
		(FORMNS,u'id'),
		(FORMNS,u'toggle'),
		(FORMNS,u'value'),
		(FORMNS,u'button-type'),
		(FORMNS,u'printable'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'image-align'),
		(OFFICENS,u'target-frame'),
		(FORMNS,u'disabled'),
		(FORMNS,u'label'),
		(FORMNS,u'default-button'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'focus-on-click'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'title'),
		(XLINKNS,u'href'),
		(FORMNS,u'name'),
		(FORMNS,u'xforms-submission'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'repeat'),
		(FORMNS,u'delay-for-repeat'),
		(FORMNS,u'image-position'),
	),
# allowed_attributes
	(FORMNS,u'checkbox'):(
		(FORMNS,u'current-state'),
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'image-align'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'label'),
		(FORMNS,u'state'),
		(FORMNS,u'data-field'),
		(FORMNS,u'is-tristate'),
		(FORMNS,u'image-position'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'visual-effect'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'tab-index'),
	),
# allowed_attributes
	(FORMNS,u'column'):(
		(FORMNS,u'text-style-name'),
		(FORMNS,u'name'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'label'),
	),
# allowed_attributes
	(FORMNS,u'combobox'):(
		(XMLNS,u'id'),
		(FORMNS,u'dropdown'),
		(FORMNS,u'current-value'),
		(FORMNS,u'list-source'),
		(FORMNS,u'list-source-type'),
		(FORMNS,u'max-length'),
		(FORMNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'convert-empty-to-null'),
		(FORMNS,u'printable'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'disabled'),
		(FORMNS,u'data-field'),
		(FORMNS,u'source-cell-range'),
		(FORMNS,u'size'),
		(FORMNS,u'auto-complete'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'title'),
		(FORMNS,u'name'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'linked-cell'),
	),
# allowed_attributes
	(FORMNS,u'connection-resource'):(
		(XLINKNS,u'href'),
	),
# allowed_attributes
	(FORMNS,u'date'):(
		(XMLNS,u'id'),
		(FORMNS,u'current-value'),
		(FORMNS,u'max-length'),
		(FORMNS,u'max-value'),
		(FORMNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(FORMNS,u'convert-empty-to-null'),
		(FORMNS,u'printable'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'spin-button'),
		(FORMNS,u'disabled'),
		(FORMNS,u'data-field'),
		(FORMNS,u'linked-cell'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'title'),
		(FORMNS,u'min-value'),
		(FORMNS,u'name'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'repeat'),
		(FORMNS,u'delay-for-repeat'),
	),
# allowed_attributes
	(FORMNS,u'file'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'printable'),
		(FORMNS,u'current-value'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'max-length'),
	),
# allowed_attributes
	(FORMNS,u'fixed-text'):(
		(FORMNS,u'for'),
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'label'),
		(FORMNS,u'multi-line'),
		(FORMNS,u'printable'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'title'),
	),
# allowed_attributes
	(FORMNS,u'form'):(
		(FORMNS,u'order'),
		(FORMNS,u'filter'),
		(FORMNS,u'master-fields'),
		(XLINKNS,u'actuate'),
		(FORMNS,u'allow-deletes'),
		(FORMNS,u'allow-updates'),
		(FORMNS,u'datasource'),
		(FORMNS,u'enctype'),
		(FORMNS,u'escape-processing'),
		(FORMNS,u'command-type'),
		(FORMNS,u'command'),
		(FORMNS,u'method'),
		(FORMNS,u'tab-cycle'),
		(OFFICENS,u'target-frame'),
		(FORMNS,u'detail-fields'),
		(FORMNS,u'allow-inserts'),
		(XLINKNS,u'type'),
		(FORMNS,u'control-implementation'),
		(XLINKNS,u'href'),
		(FORMNS,u'name'),
		(FORMNS,u'navigation-mode'),
		(FORMNS,u'apply-filter'),
		(FORMNS,u'ignore-result'),
	),
# allowed_attributes
	(FORMNS,u'formatted-text'):(
		(XMLNS,u'id'),
		(FORMNS,u'current-value'),
		(FORMNS,u'max-length'),
		(FORMNS,u'max-value'),
		(FORMNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(FORMNS,u'validation'),
		(FORMNS,u'convert-empty-to-null'),
		(FORMNS,u'printable'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'spin-button'),
		(FORMNS,u'disabled'),
		(FORMNS,u'data-field'),
		(FORMNS,u'linked-cell'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'title'),
		(FORMNS,u'min-value'),
		(FORMNS,u'name'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'repeat'),
		(FORMNS,u'delay-for-repeat'),
	),
# allowed_attributes
	(FORMNS,u'frame'):(
		(FORMNS,u'for'),
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'label'),
		(FORMNS,u'printable'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'title'),
	),
# allowed_attributes
	(FORMNS,u'generic-control'):(
		(FORMNS,u'name'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'id'),
		(XFORMSNS,u'bind'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(FORMNS,u'grid'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'tab-index'),
	),
# allowed_attributes
	(FORMNS,u'hidden'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(XFORMSNS,u'bind'),
	),
# allowed_attributes
	(FORMNS,u'image'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'image-data'),
		(OFFICENS,u'target-frame'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'tab-stop'),
		(XLINKNS,u'href'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'button-type'),
		(FORMNS,u'tab-index'),
	),
# allowed_attributes
	(FORMNS,u'image-frame'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'image-data'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'data-field'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'readonly'),
	),
# allowed_attributes
	(FORMNS,u'item'):(
		(FORMNS,u'label'),
	),
# allowed_attributes
	(FORMNS,u'list-property'):(
		(FORMNS,u'property-name'),
		(OFFICENS,u'value-type'),
	),
# allowed_attributes
	(FORMNS,u'list-value'):(
		(OFFICENS,u'string-value'),
	),
# allowed_attributes
	(FORMNS,u'listbox'):(
		(FORMNS,u'list-linkage-type'),
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'source-cell-range'),
		(FORMNS,u'multiple'),
		(FORMNS,u'data-field'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'size'),
		(FORMNS,u'list-source'),
		(FORMNS,u'list-source-type'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'bound-column'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'xforms-list-source'),
		(FORMNS,u'dropdown'),
	),
# allowed_attributes
	(FORMNS,u'number'):(
		(XMLNS,u'id'),
		(FORMNS,u'current-value'),
		(FORMNS,u'max-length'),
		(FORMNS,u'max-value'),
		(FORMNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(FORMNS,u'convert-empty-to-null'),
		(FORMNS,u'printable'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'spin-button'),
		(FORMNS,u'disabled'),
		(FORMNS,u'data-field'),
		(FORMNS,u'linked-cell'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'title'),
		(FORMNS,u'min-value'),
		(FORMNS,u'name'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'repeat'),
		(FORMNS,u'delay-for-repeat'),
	),
# allowed_attributes
	(FORMNS,u'option'):(
		(FORMNS,u'current-selected'),
		(FORMNS,u'value'),
		(FORMNS,u'label'),
		(FORMNS,u'selected'),
	),
# allowed_attributes
	(FORMNS,u'password'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'echo-char'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(FORMNS,u'convert-empty-to-null'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'max-length'),
	),
# allowed_attributes
	(FORMNS,u'properties'):(
	),
# allowed_attributes
	(FORMNS,u'property'):(
		(OFFICENS,u'value-type'),
		(OFFICENS,u'value'),
		(OFFICENS,u'date-value'),
		(FORMNS,u'property-name'),
		(OFFICENS,u'currency'),
		(OFFICENS,u'string-value'),
		(OFFICENS,u'boolean-value'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(FORMNS,u'radio'):(
		(FORMNS,u'current-selected'),
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'selected'),
		(FORMNS,u'image-align'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'label'),
		(FORMNS,u'data-field'),
		(FORMNS,u'image-position'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'visual-effect'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'tab-index'),
	),
# allowed_attributes
	(FORMNS,u'text'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'data-field'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'printable'),
		(FORMNS,u'current-value'),
		(FORMNS,u'title'),
		(FORMNS,u'convert-empty-to-null'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'max-length'),
	),
# allowed_attributes
	(FORMNS,u'textarea'):(
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'data-field'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'printable'),
		(FORMNS,u'current-value'),
		(FORMNS,u'title'),
		(FORMNS,u'convert-empty-to-null'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'max-length'),
	),
# allowed_attributes
	(FORMNS,u'time'):(
		(XMLNS,u'id'),
		(FORMNS,u'current-value'),
		(FORMNS,u'max-length'),
		(FORMNS,u'max-value'),
		(FORMNS,u'id'),
		(FORMNS,u'readonly'),
		(FORMNS,u'value'),
		(FORMNS,u'convert-empty-to-null'),
		(FORMNS,u'printable'),
		(FORMNS,u'tab-index'),
		(FORMNS,u'spin-button'),
		(FORMNS,u'disabled'),
		(FORMNS,u'data-field'),
		(FORMNS,u'linked-cell'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'control-implementation'),
		(FORMNS,u'title'),
		(FORMNS,u'min-value'),
		(FORMNS,u'name'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'repeat'),
		(FORMNS,u'delay-for-repeat'),
	),
# allowed_attributes
	(FORMNS,u'value-range'):(
		(FORMNS,u'max-value'),
		(FORMNS,u'id'),
		(FORMNS,u'control-implementation'),
		(XMLNS,u'id'),
		(FORMNS,u'repeat'),
		(FORMNS,u'delay-for-repeat'),
		(FORMNS,u'step-size'),
		(FORMNS,u'value'),
		(FORMNS,u'name'),
		(FORMNS,u'disabled'),
		(FORMNS,u'min-value'),
		(FORMNS,u'orientation'),
		(FORMNS,u'tab-stop'),
		(FORMNS,u'linked-cell'),
		(FORMNS,u'page-step-size'),
		(FORMNS,u'printable'),
		(FORMNS,u'title'),
		(XFORMSNS,u'bind'),
		(FORMNS,u'tab-index'),
	),
# allowed_attributes
	(MANIFESTNS,u'algorithm'):(
		(MANIFESTNS,u'initialisation-vector'),
		(MANIFESTNS,u'algorithm-name'),
	),
# allowed_attributes
	(MANIFESTNS,u'encryption-data'):(
		(MANIFESTNS,u'checksum-type'),
		(MANIFESTNS,u'checksum'),
	),
# allowed_attributes
	(MANIFESTNS,u'file-entry'):(
		(MANIFESTNS,u'media-type'),
		(MANIFESTNS,u'full-path'),
		(MANIFESTNS,u'version'),
		(MANIFESTNS,u'size'),
		(MANIFESTNS,u'preferred-view-mode'),
	),
# allowed_attributes
	(MANIFESTNS,u'key-derivation'):(
		(MANIFESTNS,u'salt'),
		(MANIFESTNS,u'key-derivation-name'),
		(MANIFESTNS,u'key-size'),
		(MANIFESTNS,u'iteration-count'),
	),
# allowed_attributes
	(MANIFESTNS,u'manifest'):(
	),
# allowed_attributes
	(MANIFESTNS,u'start-key-generation'):(
		(MANIFESTNS,u'key-size'),
		(MANIFESTNS,u'start-key-generation-name'),
	),
# allowed_attributes
	(METANS,u'auto-reload'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'show'),
		(METANS,u'delay'),
	),
# allowed_attributes
	(METANS,u'creation-date'):(
	),
# allowed_attributes
	(METANS,u'date-string'):(
	),
# allowed_attributes
	(METANS,u'document-statistic'):(
		(METANS,u'sentence-count'),
		(METANS,u'non-whitespace-character-count'),
		(METANS,u'word-count'),
		(METANS,u'table-count'),
		(METANS,u'cell-count'),
		(METANS,u'object-count'),
		(METANS,u'ole-object-count'),
		(METANS,u'page-count'),
		(METANS,u'draw-count'),
		(METANS,u'row-count'),
		(METANS,u'frame-count'),
		(METANS,u'paragraph-count'),
		(METANS,u'image-count'),
		(METANS,u'syllable-count'),
		(METANS,u'character-count'),
	),
# allowed_attributes
	(METANS,u'editing-cycles'):(
	),
# allowed_attributes
	(METANS,u'editing-duration'):(
	),
# allowed_attributes
	(METANS,u'generator'):(
	),
# allowed_attributes
	(METANS,u'hyperlink-behaviour'):(
		(OFFICENS,u'target-frame-name'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(METANS,u'initial-creator'):(
	),
# allowed_attributes
	(METANS,u'keyword'):(
	),
# allowed_attributes
	(METANS,u'print-date'):(
	),
# allowed_attributes
	(METANS,u'printed-by'):(
	),
# allowed_attributes
	(METANS,u'template'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'title'),
		(METANS,u'date'),
	),
# allowed_attributes
	(METANS,u'user-defined'):(
		(METANS,u'name'),
		(METANS,u'value-type'),
	),
# allowed_attributes
	(OFFICENS,u'annotation'):(
		(PRESENTATIONNS,u'style-name'),
		(TABLENS,u'end-x'),
		(XMLNS,u'id'),
		(DRAWNS,u'name'),
		(DRAWNS,u'layer'),
		(SVGNS,u'x'),
		(DRAWNS,u'caption-point-y'),
		(TEXTNS,u'anchor-page-number'),
		(DRAWNS,u'id'),
		(DRAWNS,u'z-index'),
		(DRAWNS,u'corner-radius'),
		(DRAWNS,u'transform'),
		(DRAWNS,u'caption-point-x'),
		(TABLENS,u'table-background'),
		(TEXTNS,u'anchor-type'),
		(OFFICENS,u'display'),
		(DRAWNS,u'style-name'),
		(SVGNS,u'height'),
		(OFFICENS,u'name'),
		(TABLENS,u'end-y'),
		(PRESENTATIONNS,u'class-names'),
		(SVGNS,u'width'),
		(TABLENS,u'end-cell-address'),
		(DRAWNS,u'text-style-name'),
		(SVGNS,u'y'),
		(DRAWNS,u'class-names'),
	),
# allowed_attributes
	(OFFICENS,u'annotation-end'):(
		(OFFICENS,u'name'),
	),
# allowed_attributes
	(OFFICENS,u'automatic-styles'):(
	),
# allowed_attributes
	(OFFICENS,u'binary-data'):(
	),
# allowed_attributes
	(OFFICENS,u'body'):(
	),
# allowed_attributes
	(OFFICENS,u'change-info'):(
	),
# allowed_attributes
	(OFFICENS,u'chart'):(
	),
# allowed_attributes
	(OFFICENS,u'database'):(
	),
# allowed_attributes
	(OFFICENS,u'dde-source'):(
		(OFFICENS,u'dde-item'),
		(OFFICENS,u'dde-topic'),
		(OFFICENS,u'name'),
		(OFFICENS,u'conversion-mode'),
		(OFFICENS,u'automatic-update'),
		(OFFICENS,u'dde-application'),
	),
# allowed_attributes
	(OFFICENS,u'document'):(
		(OFFICENS,u'mimetype'),
		(OFFICENS,u'version'),
		(GRDDLNS,u'transformation'),
	),
# allowed_attributes
	(OFFICENS,u'document-content'):(
		(OFFICENS,u'version'),
		(GRDDLNS,u'transformation'),
	),
# allowed_attributes
	(OFFICENS,u'document-meta'):(
		(OFFICENS,u'version'),
		(GRDDLNS,u'transformation'),
	),
# allowed_attributes
	(OFFICENS,u'document-settings'):(
		(OFFICENS,u'version'),
		(GRDDLNS,u'transformation'),
	),
# allowed_attributes
	(OFFICENS,u'document-styles'):(
		(OFFICENS,u'version'),
		(GRDDLNS,u'transformation'),
	),
# allowed_attributes
	(OFFICENS,u'drawing'):(
	),
# allowed_attributes
	(OFFICENS,u'event-listeners'):(
	),
# allowed_attributes
	(OFFICENS,u'font-face-decls'):(
	),
# allowed_attributes
	(OFFICENS,u'forms'):(
		(FORMNS,u'apply-design-mode'),
		(FORMNS,u'automatic-focus'),
	),
# allowed_attributes
	(OFFICENS,u'image'):(
	),
# allowed_attributes
	(OFFICENS,u'master-styles'):(
	),
# allowed_attributes
	(OFFICENS,u'meta'):(
	),
# allowed_attributes
	(OFFICENS,u'presentation'):(
	),
# allowed_attributes
	(OFFICENS,u'script'):(
		(SCRIPTNS,u'language'),
	),
# allowed_attributes
	(OFFICENS,u'scripts'):(
	),
# allowed_attributes
	(OFFICENS,u'settings'):(
	),
# allowed_attributes
	(OFFICENS,u'spreadsheet'):(
		(TABLENS,u'structure-protected'),
		(TABLENS,u'protection-key'),
		(TABLENS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(OFFICENS,u'styles'):(
	),
# allowed_attributes
	(OFFICENS,u'text'):(
		(TEXTNS,u'global'),
		(TEXTNS,u'use-soft-page-breaks'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'animation-group'):(
	),
# allowed_attributes
	(PRESENTATIONNS,u'animations'):(
	),
# allowed_attributes
	(PRESENTATIONNS,u'date-time'):(
	),
# allowed_attributes
	(PRESENTATIONNS,u'date-time-decl'):(
		(PRESENTATIONNS,u'name'),
		(PRESENTATIONNS,u'source'),
		(STYLENS,u'data-style-name'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'dim'):(
		(DRAWNS,u'color'),
		(DRAWNS,u'shape-id'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'event-listener'):(
		(PRESENTATIONNS,u'start-scale'),
		(XLINKNS,u'type'),
		(PRESENTATIONNS,u'verb'),
		(XLINKNS,u'show'),
		(PRESENTATIONNS,u'speed'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(PRESENTATIONNS,u'direction'),
		(PRESENTATIONNS,u'action'),
		(PRESENTATIONNS,u'effect'),
		(SCRIPTNS,u'event-name'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'footer'):(
	),
# allowed_attributes
	(PRESENTATIONNS,u'footer-decl'):(
		(PRESENTATIONNS,u'name'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'header'):(
	),
# allowed_attributes
	(PRESENTATIONNS,u'header-decl'):(
		(PRESENTATIONNS,u'name'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'hide-shape'):(
		(PRESENTATIONNS,u'start-scale'),
		(PRESENTATIONNS,u'speed'),
		(PRESENTATIONNS,u'direction'),
		(PRESENTATIONNS,u'path-id'),
		(PRESENTATIONNS,u'effect'),
		(PRESENTATIONNS,u'delay'),
		(DRAWNS,u'shape-id'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'hide-text'):(
		(PRESENTATIONNS,u'start-scale'),
		(PRESENTATIONNS,u'speed'),
		(PRESENTATIONNS,u'direction'),
		(PRESENTATIONNS,u'path-id'),
		(PRESENTATIONNS,u'effect'),
		(PRESENTATIONNS,u'delay'),
		(DRAWNS,u'shape-id'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'notes'):(
		(PRESENTATIONNS,u'use-date-time-name'),
		(DRAWNS,u'style-name'),
		(PRESENTATIONNS,u'use-footer-name'),
		(PRESENTATIONNS,u'use-header-name'),
		(STYLENS,u'page-layout-name'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'placeholder'):(
		(SVGNS,u'width'),
		(SVGNS,u'x'),
		(PRESENTATIONNS,u'object'),
		(SVGNS,u'height'),
		(SVGNS,u'y'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'play'):(
		(PRESENTATIONNS,u'speed'),
		(DRAWNS,u'shape-id'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'settings'):(
		(PRESENTATIONNS,u'start-page'),
		(PRESENTATIONNS,u'stay-on-top'),
		(PRESENTATIONNS,u'show'),
		(PRESENTATIONNS,u'start-with-navigator'),
		(PRESENTATIONNS,u'force-manual'),
		(PRESENTATIONNS,u'full-screen'),
		(PRESENTATIONNS,u'mouse-as-pen'),
		(PRESENTATIONNS,u'show-logo'),
		(PRESENTATIONNS,u'pause'),
		(PRESENTATIONNS,u'animations'),
		(PRESENTATIONNS,u'transition-on-click'),
		(PRESENTATIONNS,u'endless'),
		(PRESENTATIONNS,u'show-end-of-presentation-slide'),
		(PRESENTATIONNS,u'mouse-visible'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'show'):(
		(PRESENTATIONNS,u'name'),
		(PRESENTATIONNS,u'pages'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'show-shape'):(
		(PRESENTATIONNS,u'start-scale'),
		(PRESENTATIONNS,u'speed'),
		(PRESENTATIONNS,u'direction'),
		(PRESENTATIONNS,u'path-id'),
		(PRESENTATIONNS,u'effect'),
		(PRESENTATIONNS,u'delay'),
		(DRAWNS,u'shape-id'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'show-text'):(
		(PRESENTATIONNS,u'start-scale'),
		(PRESENTATIONNS,u'speed'),
		(PRESENTATIONNS,u'direction'),
		(PRESENTATIONNS,u'path-id'),
		(PRESENTATIONNS,u'effect'),
		(PRESENTATIONNS,u'delay'),
		(DRAWNS,u'shape-id'),
	),
# allowed_attributes
	(PRESENTATIONNS,u'sound'):(
		(XLINKNS,u'type'),
		(PRESENTATIONNS,u'play-full'),
		(XMLNS,u'id'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(SCRIPTNS,u'event-listener'):(
		(XLINKNS,u'type'),
		(SCRIPTNS,u'language'),
		(XLINKNS,u'href'),
		(SCRIPTNS,u'macro-name'),
		(XLINKNS,u'actuate'),
		(SCRIPTNS,u'event-name'),
	),
# allowed_attributes
	(STYLENS,u'background-image'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'show'),
		(STYLENS,u'position'),
		(STYLENS,u'repeat'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'href'),
		(DRAWNS,u'opacity'),
		(STYLENS,u'filter-name'),
	),
# allowed_attributes
	(STYLENS,u'chart-properties'):(
		(CHARTNS,u'connect-bars'),
		(CHARTNS,u'axis-position'),
		(TEXTNS,u'line-break'),
		(CHARTNS,u'logarithmic'),
		(CHARTNS,u'tick-marks-major-inner'),
		(CHARTNS,u'gap-width'),
		(CHARTNS,u'error-lower-indicator'),
		(CHARTNS,u'interval-minor-divisor'),
		(CHARTNS,u'deep'),
		(CHARTNS,u'reverse-direction'),
		(CHARTNS,u'maximum'),
		(CHARTNS,u'data-label-symbol'),
		(CHARTNS,u'error-upper-limit'),
		(CHARTNS,u'visible'),
		(CHARTNS,u'axis-label-position'),
		(CHARTNS,u'data-label-number'),
		(CHARTNS,u'right-angled-axes'),
		(CHARTNS,u'label-arrangement'),
		(CHARTNS,u'hole-size'),
		(CHARTNS,u'error-percentage'),
		(CHARTNS,u'text-overlap'),
		(CHARTNS,u'auto-size'),
		(CHARTNS,u'error-category'),
		(CHARTNS,u'display-label'),
		(CHARTNS,u'group-bars-per-axis'),
		(CHARTNS,u'solid-type'),
		(CHARTNS,u'treat-empty-cells'),
		(CHARTNS,u'percentage'),
		(CHARTNS,u'tick-marks-major-outer'),
		(CHARTNS,u'symbol-width'),
		(CHARTNS,u'link-data-style-to-source'),
		(CHARTNS,u'tick-marks-minor-outer'),
		(CHARTNS,u'vertical'),
		(CHARTNS,u'japanese-candle-stick'),
		(CHARTNS,u'symbol-type'),
		(CHARTNS,u'interpolation'),
		(CHARTNS,u'pie-offset'),
		(CHARTNS,u'angle-offset'),
		(CHARTNS,u'error-upper-indicator'),
		(CHARTNS,u'interval-major'),
		(CHARTNS,u'spline-resolution'),
		(CHARTNS,u'auto-position'),
		(CHARTNS,u'origin'),
		(CHARTNS,u'include-hidden-cells'),
		(CHARTNS,u'tick-mark-position'),
		(CHARTNS,u'error-margin'),
		(CHARTNS,u'tick-marks-minor-inner'),
		(CHARTNS,u'minimum'),
		(CHARTNS,u'scale-text'),
		(STYLENS,u'rotation-angle'),
		(CHARTNS,u'symbol-height'),
		(CHARTNS,u'symbol-name'),
		(CHARTNS,u'sort-by-x-values'),
		(CHARTNS,u'three-dimensional'),
		(STYLENS,u'direction'),
		(CHARTNS,u'label-position'),
		(CHARTNS,u'stacked'),
		(CHARTNS,u'regression-type'),
		(CHARTNS,u'label-position-negative'),
		(CHARTNS,u'error-lower-limit'),
		(CHARTNS,u'data-label-text'),
		(CHARTNS,u'mean-value'),
		(CHARTNS,u'series-source'),
		(CHARTNS,u'overlap'),
		(CHARTNS,u'spline-order'),
		(CHARTNS,u'lines'),
	),
# allowed_attributes
	(STYLENS,u'column'):(
		(FONS,u'start-indent'),
		(FONS,u'end-indent'),
		(STYLENS,u'rel-width'),
		(FONS,u'space-after'),
		(FONS,u'space-before'),
	),
# allowed_attributes
	(STYLENS,u'column-sep'):(
		(STYLENS,u'vertical-align'),
		(STYLENS,u'color'),
		(STYLENS,u'height'),
		(STYLENS,u'style'),
		(STYLENS,u'width'),
	),
# allowed_attributes
	(STYLENS,u'columns'):(
		(FONS,u'column-gap'),
		(FONS,u'column-count'),
	),
# allowed_attributes
	(STYLENS,u'default-page-layout'):(
	),
# allowed_attributes
	(STYLENS,u'default-style'):(
		(STYLENS,u'family'),
	),
# allowed_attributes
	(STYLENS,u'drawing-page-properties'):(
		(DRAWNS,u'fill-image-ref-point-y'),
		(PRESENTATIONNS,u'display-date-time'),
		(STYLENS,u'repeat'),
		(PRESENTATIONNS,u'background-objects-visible'),
		(PRESENTATIONNS,u'display-page-number'),
		(SMILNS,u'subtype'),
		(DRAWNS,u'tile-repeat-offset'),
		(DRAWNS,u'opacity'),
		(DRAWNS,u'fill-image-name'),
		(PRESENTATIONNS,u'display-footer'),
		(DRAWNS,u'fill-image-ref-point'),
		(DRAWNS,u'fill-image-ref-point-x'),
		(PRESENTATIONNS,u'background-visible'),
		(PRESENTATIONNS,u'transition-type'),
		(PRESENTATIONNS,u'duration'),
		(DRAWNS,u'secondary-fill-color'),
		(DRAWNS,u'fill-gradient-name'),
		(SMILNS,u'direction'),
		(DRAWNS,u'fill-hatch-name'),
		(DRAWNS,u'fill-image-height'),
		(PRESENTATIONNS,u'display-header'),
		(DRAWNS,u'fill-image-width'),
		(SMILNS,u'fadeColor'),
		(DRAWNS,u'background-size'),
		(SMILNS,u'type'),
		(DRAWNS,u'opacity-name'),
		(DRAWNS,u'fill'),
		(DRAWNS,u'gradient-step-count'),
		(DRAWNS,u'fill-color'),
		(DRAWNS,u'fill-hatch-solid'),
		(PRESENTATIONNS,u'visibility'),
		(PRESENTATIONNS,u'transition-speed'),
		(PRESENTATIONNS,u'transition-style'),
		(SVGNS,u'fill-rule'),
	),
# allowed_attributes
	(STYLENS,u'drop-cap'):(
		(STYLENS,u'lines'),
		(STYLENS,u'style-name'),
		(STYLENS,u'length'),
		(STYLENS,u'distance'),
	),
# allowed_attributes
	(STYLENS,u'font-face'):(
		(SVGNS,u'v-ideographic'),
		(SVGNS,u'slope'),
		(SVGNS,u'bbox'),
		(SVGNS,u'alphabetic'),
		(SVGNS,u'hanging'),
		(SVGNS,u'strikethrough-thickness'),
		(SVGNS,u'ascent'),
		(STYLENS,u'font-family-generic'),
		(STYLENS,u'font-adornments'),
		(SVGNS,u'mathematical'),
		(SVGNS,u'font-weight'),
		(SVGNS,u'stemh'),
		(SVGNS,u'underline-thickness'),
		(SVGNS,u'ideographic'),
		(SVGNS,u'font-variant'),
		(SVGNS,u'font-style'),
		(SVGNS,u'descent'),
		(SVGNS,u'font-stretch'),
		(SVGNS,u'stemv'),
		(SVGNS,u'x-height'),
		(SVGNS,u'font-family'),
		(SVGNS,u'strikethrough-position'),
		(SVGNS,u'units-per-em'),
		(SVGNS,u'font-size'),
		(SVGNS,u'cap-height'),
		(SVGNS,u'unicode-range'),
		(SVGNS,u'v-hanging'),
		(STYLENS,u'name'),
		(SVGNS,u'overline-thickness'),
		(SVGNS,u'v-alphabetic'),
		(SVGNS,u'widths'),
		(SVGNS,u'underline-position'),
		(SVGNS,u'accent-height'),
		(SVGNS,u'v-mathematical'),
		(SVGNS,u'panose-1'),
		(STYLENS,u'font-pitch'),
		(SVGNS,u'overline-position'),
		(STYLENS,u'font-charset'),
	),
# allowed_attributes
	(STYLENS,u'footer'):(
		(STYLENS,u'display'),
	),
# allowed_attributes
	(STYLENS,u'footer-left'):(
		(STYLENS,u'display'),
	),
# allowed_attributes
	(STYLENS,u'footer-style'):(
	),
# allowed_attributes
	(STYLENS,u'footnote-sep'):(
		(STYLENS,u'adjustment'),
		(STYLENS,u'line-style'),
		(STYLENS,u'distance-before-sep'),
		(STYLENS,u'color'),
		(STYLENS,u'distance-after-sep'),
		(STYLENS,u'rel-width'),
		(STYLENS,u'width'),
	),
# allowed_attributes
	(STYLENS,u'graphic-properties'):(
		(DRAWNS,u'fill-hatch-name'),
		(FONS,u'padding'),
		(DRAWNS,u'auto-grow-height'),
		(STYLENS,u'border-line-width-left'),
		(STYLENS,u'border-line-width-right'),
		(DRAWNS,u'shadow'),
		(TEXTNS,u'animation-steps'),
		(FONS,u'padding-bottom'),
		(STYLENS,u'overflow-behavior'),
		(DR3DNS,u'backface-culling'),
		(DRAWNS,u'start-guide'),
		(DRAWNS,u'fit-to-size'),
		(DR3DNS,u'edge-rounding'),
		(STYLENS,u'border-line-width-top'),
		(DRAWNS,u'end-line-spacing-horizontal'),
		(DRAWNS,u'stroke-dash'),
		(DR3DNS,u'normals-direction'),
		(DR3DNS,u'texture-mode'),
		(DRAWNS,u'wrap-influence-on-position'),
		(TEXTNS,u'animation-start-inside'),
		(TEXTNS,u'animation-direction'),
		(DR3DNS,u'close-front'),
		(DRAWNS,u'secondary-fill-color'),
		(DRAWNS,u'shadow-offset-y'),
		(FONS,u'clip'),
		(DRAWNS,u'decimal-places'),
		(DRAWNS,u'fill-image-width'),
		(STYLENS,u'background-transparency'),
		(STYLENS,u'horizontal-rel'),
		(DRAWNS,u'stroke-dash-names'),
		(FONS,u'margin-bottom'),
		(DRAWNS,u'opacity-name'),
		(DRAWNS,u'gamma'),
		(DRAWNS,u'draw-aspect'),
		(DRAWNS,u'parallel'),
		(FONS,u'border'),
		(STYLENS,u'vertical-rel'),
		(SVGNS,u'y'),
		(DR3DNS,u'emissive-color'),
		(DRAWNS,u'frame-display-scrollbar'),
		(DRAWNS,u'start-line-spacing-vertical'),
		(DRAWNS,u'shadow-color'),
		(SVGNS,u'fill-rule'),
		(SVGNS,u'stroke-width'),
		(STYLENS,u'wrap-contour-mode'),
		(FONS,u'padding-right'),
		(STYLENS,u'protect'),
		(STYLENS,u'run-through'),
		(FONS,u'background-color'),
		(DR3DNS,u'specular-color'),
		(STYLENS,u'print-content'),
		(DRAWNS,u'tile-repeat-offset'),
		(SVGNS,u'height'),
		(SVGNS,u'x'),
		(DR3DNS,u'texture-generation-mode-x'),
		(STYLENS,u'wrap-dynamic-threshold'),
		(FONS,u'padding-top'),
		(DRAWNS,u'fill-image-ref-point-x'),
		(DR3DNS,u'edge-rounding-mode'),
		(DR3DNS,u'texture-kind'),
		(DR3DNS,u'vertical-segments'),
		(DRAWNS,u'caption-type'),
		(DRAWNS,u'marker-start-width'),
		(FONS,u'margin-left'),
		(STYLENS,u'shrink-to-fit'),
		(DRAWNS,u'visible-area-width'),
		(DRAWNS,u'measure-vertical-align'),
		(TEXTNS,u'anchor-type'),
		(DRAWNS,u'unit'),
		(DR3DNS,u'end-angle'),
		(DR3DNS,u'horizontal-segments'),
		(DRAWNS,u'red'),
		(DRAWNS,u'textarea-vertical-align'),
		(DR3DNS,u'ambient-color'),
		(DRAWNS,u'stroke-linejoin'),
		(TEXTNS,u'animation-delay'),
		(DRAWNS,u'fill'),
		(STYLENS,u'editable'),
		(DRAWNS,u'gradient-step-count'),
		(DRAWNS,u'fill-color'),
		(DRAWNS,u'stroke'),
		(DRAWNS,u'visible-area-top'),
		(DRAWNS,u'frame-margin-vertical'),
		(DRAWNS,u'fill-image-ref-point-y'),
		(DRAWNS,u'show-unit'),
		(DRAWNS,u'marker-end'),
		(SVGNS,u'stroke-color'),
		(DRAWNS,u'caption-angle-type'),
		(DRAWNS,u'marker-end-center'),
		(FONS,u'margin'),
		(FONS,u'border-top'),
		(DR3DNS,u'normals-kind'),
		(DRAWNS,u'caption-escape'),
		(DR3DNS,u'lighting-mode'),
		(DR3DNS,u'texture-filter'),
		(SVGNS,u'stroke-linecap'),
		(DRAWNS,u'textarea-horizontal-align'),
		(DRAWNS,u'fill-image-ref-point'),
		(FONS,u'margin-right'),
		(TEXTNS,u'anchor-page-number'),
		(FONS,u'min-height'),
		(STYLENS,u'border-line-width'),
		(DRAWNS,u'end-guide'),
		(DRAWNS,u'luminance'),
		(TEXTNS,u'animation-repeat'),
		(STYLENS,u'repeat'),
		(DR3DNS,u'texture-generation-mode-y'),
		(DRAWNS,u'blue'),
		(DRAWNS,u'marker-end-width'),
		(DRAWNS,u'fill-gradient-name'),
		(DRAWNS,u'green'),
		(DRAWNS,u'measure-align'),
		(FONS,u'max-height'),
		(DRAWNS,u'frame-display-border'),
		(DRAWNS,u'auto-grow-width'),
		(FONS,u'border-bottom'),
		(TEXTNS,u'animation-stop-inside'),
		(STYLENS,u'rel-width'),
		(STYLENS,u'shadow'),
		(FONS,u'border-right'),
		(FONS,u'min-width'),
		(DRAWNS,u'opacity'),
		(FONS,u'padding-left'),
		(DRAWNS,u'end-line-spacing-vertical'),
		(SVGNS,u'width'),
		(DRAWNS,u'guide-overhang'),
		(DRAWNS,u'ole-draw-aspect'),
		(DRAWNS,u'color-inversion'),
		(DRAWNS,u'placing'),
		(DR3DNS,u'close-back'),
		(DRAWNS,u'start-line-spacing-horizontal'),
		(DRAWNS,u'image-opacity'),
		(STYLENS,u'wrap-contour'),
		(DRAWNS,u'fit-to-contour'),
		(DRAWNS,u'color-mode'),
		(DRAWNS,u'symbol-color'),
		(DRAWNS,u'caption-gap'),
		(DRAWNS,u'frame-margin-horizontal'),
		(DRAWNS,u'caption-line-length'),
		(FONS,u'border-left'),
		(FONS,u'max-width'),
		(DRAWNS,u'fill-image-name'),
		(DR3DNS,u'back-scale'),
		(DRAWNS,u'caption-fit-line-length'),
		(SVGNS,u'stroke-opacity'),
		(DRAWNS,u'shadow-opacity'),
		(DRAWNS,u'shadow-offset-x'),
		(STYLENS,u'mirror'),
		(DRAWNS,u'visible-area-height'),
		(FONS,u'margin-top'),
		(DRAWNS,u'fill-image-height'),
		(STYLENS,u'vertical-pos'),
		(DRAWNS,u'caption-escape-direction'),
		(STYLENS,u'horizontal-pos'),
		(STYLENS,u'flow-with-text'),
		(TEXTNS,u'animation'),
		(DRAWNS,u'caption-angle'),
		(DRAWNS,u'contrast'),
		(DR3DNS,u'diffuse-color'),
		(STYLENS,u'rel-height'),
		(DRAWNS,u'marker-start-center'),
		(DR3DNS,u'shadow'),
		(STYLENS,u'number-wrapped-paragraphs'),
		(STYLENS,u'border-line-width-bottom'),
		(STYLENS,u'writing-mode'),
		(DRAWNS,u'guide-distance'),
		(DR3DNS,u'depth'),
		(DRAWNS,u'marker-start'),
		(STYLENS,u'wrap'),
		(DRAWNS,u'fill-hatch-solid'),
		(DRAWNS,u'line-distance'),
		(DRAWNS,u'visible-area-left'),
		(FONS,u'wrap-option'),
		(DR3DNS,u'shininess'),
	),
# allowed_attributes
	(STYLENS,u'handout-master'):(
		(DRAWNS,u'style-name'),
		(PRESENTATIONNS,u'presentation-page-layout-name'),
		(PRESENTATIONNS,u'use-date-time-name'),
		(PRESENTATIONNS,u'use-header-name'),
		(STYLENS,u'page-layout-name'),
		(PRESENTATIONNS,u'use-footer-name'),
	),
# allowed_attributes
	(STYLENS,u'header'):(
		(STYLENS,u'display'),
	),
# allowed_attributes
	(STYLENS,u'header-footer-properties'):(
		(FONS,u'padding'),
		(FONS,u'padding-right'),
		(FONS,u'margin'),
		(FONS,u'border-top'),
		(STYLENS,u'border-line-width-right'),
		(FONS,u'background-color'),
		(FONS,u'border-left'),
		(STYLENS,u'border-line-width-top'),
		(FONS,u'padding-top'),
		(FONS,u'padding-bottom'),
		(FONS,u'margin-top'),
		(STYLENS,u'border-line-width'),
		(FONS,u'margin-right'),
		(FONS,u'border-bottom'),
		(SVGNS,u'height'),
		(STYLENS,u'border-line-width-left'),
		(FONS,u'margin-bottom'),
		(FONS,u'min-height'),
		(STYLENS,u'dynamic-spacing'),
		(STYLENS,u'shadow'),
		(FONS,u'border-right'),
		(FONS,u'border'),
		(STYLENS,u'border-line-width-bottom'),
		(FONS,u'margin-left'),
		(FONS,u'padding-left'),
	),
# allowed_attributes
	(STYLENS,u'header-left'):(
		(STYLENS,u'display'),
	),
# allowed_attributes
	(STYLENS,u'header-style'):(
	),
# allowed_attributes
	(STYLENS,u'list-level-label-alignment'):(
		(FONS,u'text-indent'),
		(TEXTNS,u'label-followed-by'),
		(TEXTNS,u'list-tab-stop-position'),
		(FONS,u'margin-left'),
	),
# allowed_attributes
	(STYLENS,u'list-level-properties'):(
		(STYLENS,u'font-name'),
		(TEXTNS,u'space-before'),
		(FONS,u'text-align'),
		(STYLENS,u'vertical-rel'),
		(TEXTNS,u'list-level-position-and-space-mode'),
		(STYLENS,u'vertical-pos'),
		(TEXTNS,u'min-label-distance'),
		(FONS,u'height'),
		(TEXTNS,u'min-label-width'),
		(SVGNS,u'y'),
		(FONS,u'width'),
	),
# allowed_attributes
	(STYLENS,u'map'):(
		(STYLENS,u'condition'),
		(STYLENS,u'apply-style-name'),
		(STYLENS,u'base-cell-address'),
	),
# allowed_attributes
	(STYLENS,u'master-page'):(
		(DRAWNS,u'style-name'),
		(STYLENS,u'name'),
		(STYLENS,u'page-layout-name'),
		(STYLENS,u'next-style-name'),
		(STYLENS,u'display-name'),
	),
# allowed_attributes
	(STYLENS,u'page-layout'):(
		(STYLENS,u'name'),
		(STYLENS,u'page-usage'),
	),
# allowed_attributes
	(STYLENS,u'page-layout-properties'):(
		(STYLENS,u'num-suffix'),
		(FONS,u'padding'),
		(STYLENS,u'scale-to-pages'),
		(FONS,u'padding-right'),
		(FONS,u'margin'),
		(FONS,u'border-top'),
		(STYLENS,u'num-letter-sync'),
		(FONS,u'background-color'),
		(STYLENS,u'layout-grid-display'),
		(STYLENS,u'print-orientation'),
		(FONS,u'border-right'),
		(STYLENS,u'writing-mode'),
		(STYLENS,u'num-prefix'),
		(STYLENS,u'border-line-width-top'),
		(STYLENS,u'footnote-max-height'),
		(FONS,u'padding-top'),
		(STYLENS,u'layout-grid-color'),
		(FONS,u'margin-left'),
		(STYLENS,u'paper-tray-name'),
		(STYLENS,u'layout-grid-ruby-height'),
		(STYLENS,u'layout-grid-ruby-below'),
		(FONS,u'margin-top'),
		(STYLENS,u'border-line-width'),
		(STYLENS,u'scale-to'),
		(STYLENS,u'layout-grid-base-width'),
		(FONS,u'margin-right'),
		(FONS,u'page-height'),
		(STYLENS,u'border-line-width-right'),
		(FONS,u'border-bottom'),
		(STYLENS,u'layout-grid-mode'),
		(FONS,u'padding-bottom'),
		(STYLENS,u'layout-grid-snap-to'),
		(STYLENS,u'print'),
		(STYLENS,u'table-centering'),
		(STYLENS,u'layout-grid-standard-mode'),
		(STYLENS,u'print-page-order'),
		(FONS,u'page-width'),
		(STYLENS,u'border-line-width-left'),
		(FONS,u'margin-bottom'),
		(STYLENS,u'shadow'),
		(STYLENS,u'first-page-number'),
		(FONS,u'border-left'),
		(FONS,u'border'),
		(STYLENS,u'border-line-width-bottom'),
		(STYLENS,u'layout-grid-print'),
		(STYLENS,u'num-format'),
		(STYLENS,u'register-truth-ref-style-name'),
		(FONS,u'padding-left'),
		(STYLENS,u'layout-grid-base-height'),
		(STYLENS,u'layout-grid-lines'),
	),
# allowed_attributes
	(STYLENS,u'paragraph-properties'):(
		(TEXTNS,u'number-lines'),
		(FONS,u'padding'),
		(FONS,u'border-right'),
		(STYLENS,u'justify-single-word'),
		(FONS,u'padding-right'),
		(FONS,u'margin'),
		(STYLENS,u'register-true'),
		(FONS,u'text-align'),
		(FONS,u'background-color'),
		(FONS,u'text-align-last'),
		(FONS,u'padding-bottom'),
		(FONS,u'break-before'),
		(STYLENS,u'writing-mode'),
		(STYLENS,u'writing-mode-automatic'),
		(FONS,u'break-after'),
		(STYLENS,u'border-line-width-top'),
		(FONS,u'padding-top'),
		(FONS,u'hyphenation-keep'),
		(FONS,u'margin-right'),
		(FONS,u'line-height'),
		(FONS,u'margin-top'),
		(STYLENS,u'border-line-width'),
		(FONS,u'border-top'),
		(STYLENS,u'join-border'),
		(FONS,u'margin-left'),
		(STYLENS,u'border-line-width-right'),
		(STYLENS,u'line-break'),
		(FONS,u'text-indent'),
		(STYLENS,u'page-number'),
		(STYLENS,u'text-autospace'),
		(FONS,u'widows'),
		(STYLENS,u'border-line-width-bottom'),
		(STYLENS,u'background-transparency'),
		(STYLENS,u'punctuation-wrap'),
		(FONS,u'border-bottom'),
		(STYLENS,u'auto-text-indent'),
		(FONS,u'margin-bottom'),
		(STYLENS,u'vertical-align'),
		(STYLENS,u'shadow'),
		(FONS,u'hyphenation-ladder-count'),
		(STYLENS,u'line-height-at-least'),
		(FONS,u'border-left'),
		(STYLENS,u'line-spacing'),
		(FONS,u'border'),
		(FONS,u'keep-together'),
		(STYLENS,u'tab-stop-distance'),
		(TEXTNS,u'line-number'),
		(STYLENS,u'font-independent-line-spacing'),
		(STYLENS,u'border-line-width-left'),
		(FONS,u'keep-with-next'),
		(FONS,u'orphans'),
		(FONS,u'padding-left'),
		(STYLENS,u'snap-to-layout-grid'),
	),
# allowed_attributes
	(STYLENS,u'presentation-page-layout'):(
		(STYLENS,u'name'),
		(STYLENS,u'display-name'),
	),
# allowed_attributes
	(STYLENS,u'region-center'):(
	),
# allowed_attributes
	(STYLENS,u'region-left'):(
	),
# allowed_attributes
	(STYLENS,u'region-right'):(
	),
# allowed_attributes
	(STYLENS,u'ruby-properties'):(
		(STYLENS,u'ruby-align'),
		(STYLENS,u'ruby-position'),
	),
# allowed_attributes
	(STYLENS,u'section-properties'):(
		(STYLENS,u'editable'),
		(FONS,u'margin-right'),
		(STYLENS,u'protect'),
		(FONS,u'background-color'),
		(FONS,u'margin-left'),
		(TEXTNS,u'dont-balance-text-columns'),
		(STYLENS,u'writing-mode'),
	),
# allowed_attributes
	(STYLENS,u'style'):(
		(STYLENS,u'family'),
		(STYLENS,u'name'),
		(STYLENS,u'list-style-name'),
		(STYLENS,u'default-outline-level'),
		(STYLENS,u'auto-update'),
		(STYLENS,u'class'),
		(STYLENS,u'master-page-name'),
		(STYLENS,u'next-style-name'),
		(STYLENS,u'percentage-data-style-name'),
		(STYLENS,u'data-style-name'),
		(STYLENS,u'parent-style-name'),
		(STYLENS,u'list-level'),
		(STYLENS,u'display-name'),
	),
# allowed_attributes
	(STYLENS,u'tab-stop'):(
		(STYLENS,u'leader-width'),
		(STYLENS,u'position'),
		(STYLENS,u'leader-color'),
		(STYLENS,u'leader-type'),
		(STYLENS,u'type'),
		(STYLENS,u'leader-text-style'),
		(STYLENS,u'char'),
		(STYLENS,u'leader-style'),
		(STYLENS,u'leader-text'),
	),
# allowed_attributes
	(STYLENS,u'tab-stops'):(
	),
# allowed_attributes
	(STYLENS,u'table-cell-properties'):(
		(FONS,u'padding'),
		(FONS,u'padding-right'),
		(STYLENS,u'border-line-width-bottom'),
		(FONS,u'border-top'),
		(STYLENS,u'border-line-width-right'),
		(STYLENS,u'repeat-content'),
		(FONS,u'background-color'),
		(FONS,u'border-right'),
		(STYLENS,u'diagonal-tl-br'),
		(STYLENS,u'print-content'),
		(STYLENS,u'border-line-width-top'),
		(FONS,u'padding-top'),
		(STYLENS,u'decimal-places'),
		(STYLENS,u'diagonal-bl-tr-widths'),
		(STYLENS,u'diagonal-bl-tr'),
		(STYLENS,u'direction'),
		(STYLENS,u'border-line-width'),
		(STYLENS,u'diagonal-tl-br-widths'),
		(FONS,u'padding-bottom'),
		(STYLENS,u'rotation-angle'),
		(STYLENS,u'vertical-align'),
		(STYLENS,u'text-align-source'),
		(STYLENS,u'cell-protect'),
		(FONS,u'border-bottom'),
		(STYLENS,u'border-line-width-left'),
		(STYLENS,u'writing-mode'),
		(STYLENS,u'rotation-align'),
		(STYLENS,u'shadow'),
		(STYLENS,u'glyph-orientation-vertical'),
		(FONS,u'border-left'),
		(FONS,u'border'),
		(FONS,u'padding-left'),
		(STYLENS,u'shrink-to-fit'),
		(FONS,u'wrap-option'),
	),
# allowed_attributes
	(STYLENS,u'table-column-properties'):(
		(FONS,u'break-before'),
		(FONS,u'break-after'),
		(STYLENS,u'use-optimal-column-width'),
		(STYLENS,u'rel-column-width'),
		(STYLENS,u'column-width'),
	),
# allowed_attributes
	(STYLENS,u'table-properties'):(
		(STYLENS,u'writing-mode'),
		(FONS,u'margin-right'),
		(STYLENS,u'may-break-between-rows'),
		(FONS,u'margin'),
		(FONS,u'margin-top'),
		(FONS,u'keep-with-next'),
		(FONS,u'break-before'),
		(FONS,u'background-color'),
		(FONS,u'margin-left'),
		(FONS,u'break-after'),
		(TABLENS,u'border-model'),
		(TABLENS,u'align'),
		(FONS,u'margin-bottom'),
		(STYLENS,u'page-number'),
		(TABLENS,u'display'),
		(STYLENS,u'rel-width'),
		(STYLENS,u'shadow'),
		(STYLENS,u'width'),
	),
# allowed_attributes
	(STYLENS,u'table-row-properties'):(
		(STYLENS,u'use-optimal-row-height'),
		(FONS,u'keep-together'),
		(FONS,u'background-color'),
		(FONS,u'break-before'),
		(STYLENS,u'min-row-height'),
		(STYLENS,u'row-height'),
		(FONS,u'break-after'),
	),
# allowed_attributes
	(STYLENS,u'text-properties'):(
		(STYLENS,u'text-combine-start-char'),
		(STYLENS,u'text-line-through-type'),
		(FONS,u'font-style'),
		(STYLENS,u'language-complex'),
		(FONS,u'text-transform'),
		(FONS,u'color'),
		(FONS,u'background-color'),
		(FONS,u'hyphenate'),
		(STYLENS,u'text-overline-type'),
		(FONS,u'font-variant'),
		(STYLENS,u'rfc-language-tag'),
		(STYLENS,u'text-overline-mode'),
		(STYLENS,u'font-style-name-asian'),
		(STYLENS,u'font-family-generic-asian'),
		(STYLENS,u'country-asian'),
		(STYLENS,u'text-rotation-scale'),
		(STYLENS,u'text-underline-style'),
		(STYLENS,u'letter-kerning'),
		(STYLENS,u'rfc-language-tag-asian'),
		(STYLENS,u'text-scale'),
		(FONS,u'text-shadow'),
		(STYLENS,u'text-line-through-width'),
		(STYLENS,u'font-weight-complex'),
		(STYLENS,u'font-pitch-asian'),
		(STYLENS,u'font-style-asian'),
		(STYLENS,u'font-size-complex'),
		(FONS,u'font-weight'),
		(STYLENS,u'font-style-complex'),
		(STYLENS,u'text-overline-style'),
		(STYLENS,u'text-underline-color'),
		(TEXTNS,u'display'),
		(STYLENS,u'language-asian'),
		(STYLENS,u'country-complex'),
		(FONS,u'font-size'),
		(STYLENS,u'text-underline-width'),
		(STYLENS,u'font-name-asian'),
		(STYLENS,u'text-line-through-mode'),
		(STYLENS,u'font-charset-complex'),
		(STYLENS,u'text-outline'),
		(STYLENS,u'font-size-rel-complex'),
		(STYLENS,u'script-asian'),
		(STYLENS,u'text-line-through-color'),
		(STYLENS,u'font-size-asian'),
		(STYLENS,u'rfc-language-tag-complex'),
		(FONS,u'country'),
		(TEXTNS,u'condition'),
		(STYLENS,u'font-size-rel'),
		(STYLENS,u'text-line-through-text'),
		(FONS,u'letter-spacing'),
		(STYLENS,u'text-combine'),
		(FONS,u'hyphenation-push-char-count'),
		(STYLENS,u'font-family-complex'),
		(STYLENS,u'text-underline-mode'),
		(STYLENS,u'font-style-name'),
		(FONS,u'language'),
		(STYLENS,u'script-complex'),
		(STYLENS,u'font-family-asian'),
		(FONS,u'hyphenation-remain-char-count'),
		(STYLENS,u'text-underline-type'),
		(STYLENS,u'use-window-font-color'),
		(STYLENS,u'text-position'),
		(STYLENS,u'text-overline-color'),
		(STYLENS,u'text-overline-width'),
		(STYLENS,u'font-family-generic-complex'),
		(STYLENS,u'font-family-generic'),
		(STYLENS,u'script-type'),
		(STYLENS,u'font-name'),
		(STYLENS,u'text-line-through-style'),
		(STYLENS,u'text-combine-end-char'),
		(STYLENS,u'font-charset'),
		(FONS,u'script'),
		(STYLENS,u'text-rotation-angle'),
		(STYLENS,u'text-line-through-text-style'),
		(STYLENS,u'font-pitch-complex'),
		(STYLENS,u'font-charset-asian'),
		(STYLENS,u'font-pitch'),
		(STYLENS,u'font-name-complex'),
		(STYLENS,u'font-weight-asian'),
		(STYLENS,u'font-style-name-complex'),
		(STYLENS,u'text-emphasize'),
		(STYLENS,u'font-relief'),
		(STYLENS,u'text-blinking'),
		(FONS,u'font-family'),
		(STYLENS,u'font-size-rel-asian'),
	),
# allowed_attributes
	(SVGNS,u'definition-src'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
	),
# allowed_attributes
	(SVGNS,u'desc'):(
	),
# allowed_attributes
	(SVGNS,u'font-face-format'):(
		(SVGNS,u'string'),
	),
# allowed_attributes
	(SVGNS,u'font-face-name'):(
		(SVGNS,u'name'),
	),
# allowed_attributes
	(SVGNS,u'font-face-src'):(
	),
# allowed_attributes
	(SVGNS,u'font-face-uri'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
	),
# allowed_attributes
	(SVGNS,u'linearGradient'):(
		(SVGNS,u'x1'),
		(SVGNS,u'y2'),
		(SVGNS,u'gradientTransform'),
		(SVGNS,u'spreadMethod'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(SVGNS,u'x2'),
		(SVGNS,u'gradientUnits'),
		(SVGNS,u'y1'),
	),
# allowed_attributes
	(SVGNS,u'radialGradient'):(
		(SVGNS,u'gradientTransform'),
		(SVGNS,u'spreadMethod'),
		(SVGNS,u'fy'),
		(DRAWNS,u'name'),
		(DRAWNS,u'display-name'),
		(SVGNS,u'fx'),
		(SVGNS,u'r'),
		(SVGNS,u'gradientUnits'),
		(SVGNS,u'cx'),
		(SVGNS,u'cy'),
	),
# allowed_attributes
	(SVGNS,u'stop'):(
		(SVGNS,u'offset'),
		(SVGNS,u'stop-color'),
		(SVGNS,u'stop-opacity'),
	),
# allowed_attributes
	(SVGNS,u'title'):(
	),
# allowed_attributes
	(TABLENS,u'background'):(
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'body'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'calculation-settings'):(
		(TABLENS,u'use-regular-expressions'),
		(TABLENS,u'use-wildcards'),
		(TABLENS,u'case-sensitive'),
		(TABLENS,u'search-criteria-must-apply-to-whole-cell'),
		(TABLENS,u'automatic-find-labels'),
		(TABLENS,u'precision-as-shown'),
		(TABLENS,u'null-year'),
	),
# allowed_attributes
	(TABLENS,u'cell-address'):(
		(TABLENS,u'table'),
		(TABLENS,u'column'),
		(TABLENS,u'row'),
	),
# allowed_attributes
	(TABLENS,u'cell-content-change'):(
		(TABLENS,u'acceptance-state'),
		(TABLENS,u'id'),
		(TABLENS,u'rejecting-change-id'),
	),
# allowed_attributes
	(TABLENS,u'cell-content-deletion'):(
		(TABLENS,u'id'),
	),
# allowed_attributes
	(TABLENS,u'cell-range-source'):(
		(TABLENS,u'last-row-spanned'),
		(XLINKNS,u'type'),
		(TABLENS,u'filter-name'),
		(XLINKNS,u'href'),
		(TABLENS,u'filter-options'),
		(XLINKNS,u'actuate'),
		(TABLENS,u'name'),
		(TABLENS,u'last-column-spanned'),
		(TABLENS,u'refresh-delay'),
	),
# allowed_attributes
	(TABLENS,u'change-deletion'):(
		(TABLENS,u'id'),
	),
# allowed_attributes
	(TABLENS,u'change-track-table-cell'):(
		(OFFICENS,u'string-value'),
		(OFFICENS,u'value'),
		(OFFICENS,u'value-type'),
		(TABLENS,u'formula'),
		(OFFICENS,u'date-value'),
		(TABLENS,u'cell-address'),
		(TABLENS,u'matrix-covered'),
		(TABLENS,u'number-matrix-rows-spanned'),
		(OFFICENS,u'currency'),
		(TABLENS,u'number-matrix-columns-spanned'),
		(OFFICENS,u'boolean-value'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(TABLENS,u'consolidation'):(
		(TABLENS,u'use-labels'),
		(TABLENS,u'link-to-source-data'),
		(TABLENS,u'function'),
		(TABLENS,u'source-cell-range-addresses'),
		(TABLENS,u'target-cell-address'),
	),
# allowed_attributes
	(TABLENS,u'content-validation'):(
		(TABLENS,u'condition'),
		(TABLENS,u'display-list'),
		(TABLENS,u'name'),
		(TABLENS,u'base-cell-address'),
		(TABLENS,u'allow-empty-cell'),
	),
# allowed_attributes
	(TABLENS,u'content-validations'):(
	),
# allowed_attributes
	(TABLENS,u'covered-table-cell'):(
		(XHTMLNS,u'about'),
		(XHTMLNS,u'property'),
		(OFFICENS,u'value-type'),
		(OFFICENS,u'value'),
		(TABLENS,u'content-validation-name'),
		(TABLENS,u'formula'),
		(TABLENS,u'style-name'),
		(XHTMLNS,u'content'),
		(TABLENS,u'protect'),
		(XMLNS,u'id'),
		(OFFICENS,u'currency'),
		(OFFICENS,u'string-value'),
		(TABLENS,u'protected'),
		(XHTMLNS,u'datatype'),
		(OFFICENS,u'boolean-value'),
		(OFFICENS,u'date-value'),
		(TABLENS,u'number-columns-repeated'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(TABLENS,u'cut-offs'):(
	),
# allowed_attributes
	(TABLENS,u'data-pilot-display-info'):(
		(TABLENS,u'data-field'),
		(TABLENS,u'member-count'),
		(TABLENS,u'display-member-mode'),
		(TABLENS,u'enabled'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-field'):(
		(TABLENS,u'selected-page'),
		(TABLENS,u'is-data-layout-field'),
		(TABLENS,u'used-hierarchy'),
		(TABLENS,u'source-field-name'),
		(TABLENS,u'function'),
		(TABLENS,u'orientation'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-field-reference'):(
		(TABLENS,u'member-name'),
		(TABLENS,u'type'),
		(TABLENS,u'field-name'),
		(TABLENS,u'member-type'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-group'):(
		(TABLENS,u'name'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-group-member'):(
		(TABLENS,u'name'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-groups'):(
		(TABLENS,u'start'),
		(TABLENS,u'date-end'),
		(TABLENS,u'date-start'),
		(TABLENS,u'step'),
		(TABLENS,u'source-field-name'),
		(TABLENS,u'end'),
		(TABLENS,u'grouped-by'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-layout-info'):(
		(TABLENS,u'layout-mode'),
		(TABLENS,u'add-empty-lines'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-level'):(
		(TABLENS,u'show-empty'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-member'):(
		(TABLENS,u'display'),
		(TABLENS,u'name'),
		(TABLENS,u'show-details'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-members'):(
	),
# allowed_attributes
	(TABLENS,u'data-pilot-sort-info'):(
		(TABLENS,u'data-field'),
		(TABLENS,u'order'),
		(TABLENS,u'sort-mode'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-subtotal'):(
		(TABLENS,u'function'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-subtotals'):(
	),
# allowed_attributes
	(TABLENS,u'data-pilot-table'):(
		(TABLENS,u'drill-down-on-double-click'),
		(TABLENS,u'buttons'),
		(TABLENS,u'identify-categories'),
		(TABLENS,u'ignore-empty-rows'),
		(TABLENS,u'show-filter-button'),
		(TABLENS,u'grand-total'),
		(TABLENS,u'name'),
		(TABLENS,u'application-data'),
		(TABLENS,u'target-range-address'),
	),
# allowed_attributes
	(TABLENS,u'data-pilot-tables'):(
	),
# allowed_attributes
	(TABLENS,u'database-range'):(
		(TABLENS,u'target-range-address'),
		(TABLENS,u'is-selection'),
		(TABLENS,u'refresh-delay'),
		(TABLENS,u'display-filter-buttons'),
		(TABLENS,u'on-update-keep-size'),
		(TABLENS,u'orientation'),
		(TABLENS,u'on-update-keep-styles'),
		(TABLENS,u'name'),
		(TABLENS,u'contains-header'),
		(TABLENS,u'has-persistent-data'),
	),
# allowed_attributes
	(TABLENS,u'database-ranges'):(
	),
# allowed_attributes
	(TABLENS,u'database-source-query'):(
		(TABLENS,u'query-name'),
		(TABLENS,u'database-name'),
	),
# allowed_attributes
	(TABLENS,u'database-source-sql'):(
		(TABLENS,u'parse-sql-statement'),
		(TABLENS,u'sql-statement'),
		(TABLENS,u'database-name'),
	),
# allowed_attributes
	(TABLENS,u'database-source-table'):(
		(TABLENS,u'database-table-name'),
		(TABLENS,u'database-name'),
	),
# allowed_attributes
	(TABLENS,u'dde-link'):(
	),
# allowed_attributes
	(TABLENS,u'dde-links'):(
	),
# allowed_attributes
	(TABLENS,u'deletion'):(
		(TABLENS,u'acceptance-state'),
		(TABLENS,u'position'),
		(TABLENS,u'rejecting-change-id'),
		(TABLENS,u'multi-deletion-spanned'),
		(TABLENS,u'table'),
		(TABLENS,u'id'),
		(TABLENS,u'type'),
	),
# allowed_attributes
	(TABLENS,u'deletions'):(
	),
# allowed_attributes
	(TABLENS,u'dependencies'):(
	),
# allowed_attributes
	(TABLENS,u'dependency'):(
		(TABLENS,u'id'),
	),
# allowed_attributes
	(TABLENS,u'desc'):(
	),
# allowed_attributes
	(TABLENS,u'detective'):(
	),
# allowed_attributes
	(TABLENS,u'error-macro'):(
		(TABLENS,u'execute'),
	),
# allowed_attributes
	(TABLENS,u'error-message'):(
		(TABLENS,u'message-type'),
		(TABLENS,u'display'),
		(TABLENS,u'title'),
	),
# allowed_attributes
	(TABLENS,u'even-columns'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'even-rows'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'filter'):(
		(TABLENS,u'condition-source-range-address'),
		(TABLENS,u'display-duplicates'),
		(TABLENS,u'target-range-address'),
		(TABLENS,u'condition-source'),
	),
# allowed_attributes
	(TABLENS,u'filter-and'):(
	),
# allowed_attributes
	(TABLENS,u'filter-condition'):(
		(TABLENS,u'value'),
		(TABLENS,u'operator'),
		(TABLENS,u'case-sensitive'),
		(TABLENS,u'field-number'),
		(TABLENS,u'data-type'),
	),
# allowed_attributes
	(TABLENS,u'filter-or'):(
	),
# allowed_attributes
	(TABLENS,u'filter-set-item'):(
		(TABLENS,u'value'),
	),
# allowed_attributes
	(TABLENS,u'first-column'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'first-row'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'help-message'):(
		(TABLENS,u'display'),
		(TABLENS,u'title'),
	),
# allowed_attributes
	(TABLENS,u'highlighted-range'):(
		(TABLENS,u'contains-error'),
		(TABLENS,u'cell-range-address'),
		(TABLENS,u'direction'),
		(TABLENS,u'marked-invalid'),
	),
# allowed_attributes
	(TABLENS,u'insertion'):(
		(TABLENS,u'count'),
		(TABLENS,u'acceptance-state'),
		(TABLENS,u'position'),
		(TABLENS,u'rejecting-change-id'),
		(TABLENS,u'table'),
		(TABLENS,u'id'),
		(TABLENS,u'type'),
	),
# allowed_attributes
	(TABLENS,u'insertion-cut-off'):(
		(TABLENS,u'position'),
		(TABLENS,u'id'),
	),
# allowed_attributes
	(TABLENS,u'iteration'):(
		(TABLENS,u'status'),
		(TABLENS,u'maximum-difference'),
		(TABLENS,u'steps'),
	),
# allowed_attributes
	(TABLENS,u'label-range'):(
		(TABLENS,u'orientation'),
		(TABLENS,u'data-cell-range-address'),
		(TABLENS,u'label-cell-range-address'),
	),
# allowed_attributes
	(TABLENS,u'label-ranges'):(
	),
# allowed_attributes
	(TABLENS,u'last-column'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'last-row'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'movement'):(
		(TABLENS,u'acceptance-state'),
		(TABLENS,u'id'),
		(TABLENS,u'rejecting-change-id'),
	),
# allowed_attributes
	(TABLENS,u'movement-cut-off'):(
		(TABLENS,u'position'),
		(TABLENS,u'start-position'),
		(TABLENS,u'end-position'),
	),
# allowed_attributes
	(TABLENS,u'named-expression'):(
		(TABLENS,u'name'),
		(TABLENS,u'base-cell-address'),
		(TABLENS,u'expression'),
	),
# allowed_attributes
	(TABLENS,u'named-expressions'):(
	),
# allowed_attributes
	(TABLENS,u'named-range'):(
		(TABLENS,u'cell-range-address'),
		(TABLENS,u'name'),
		(TABLENS,u'base-cell-address'),
		(TABLENS,u'range-usable-as'),
	),
# allowed_attributes
	(TABLENS,u'null-date'):(
		(TABLENS,u'value-type'),
		(TABLENS,u'date-value'),
	),
# allowed_attributes
	(TABLENS,u'odd-columns'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'odd-rows'):(
		(TABLENS,u'paragraph-style-name'),
		(TABLENS,u'style-name'),
	),
# allowed_attributes
	(TABLENS,u'operation'):(
		(TABLENS,u'index'),
		(TABLENS,u'name'),
	),
# allowed_attributes
	(TABLENS,u'previous'):(
		(TABLENS,u'id'),
	),
# allowed_attributes
	(TABLENS,u'scenario'):(
		(TABLENS,u'comment'),
		(TABLENS,u'copy-formulas'),
		(TABLENS,u'protected'),
		(TABLENS,u'is-active'),
		(TABLENS,u'copy-back'),
		(TABLENS,u'display-border'),
		(TABLENS,u'scenario-ranges'),
		(TABLENS,u'border-color'),
		(TABLENS,u'copy-styles'),
	),
# allowed_attributes
	(TABLENS,u'shapes'):(
	),
# allowed_attributes
	(TABLENS,u'sort'):(
		(TABLENS,u'algorithm'),
		(TABLENS,u'embedded-number-behavior'),
		(TABLENS,u'bind-styles-to-content'),
		(TABLENS,u'rfc-language-tag'),
		(TABLENS,u'script'),
		(TABLENS,u'language'),
		(TABLENS,u'case-sensitive'),
		(TABLENS,u'country'),
		(TABLENS,u'target-range-address'),
	),
# allowed_attributes
	(TABLENS,u'sort-by'):(
		(TABLENS,u'order'),
		(TABLENS,u'field-number'),
		(TABLENS,u'data-type'),
	),
# allowed_attributes
	(TABLENS,u'sort-groups'):(
		(TABLENS,u'order'),
		(TABLENS,u'data-type'),
	),
# allowed_attributes
	(TABLENS,u'source-cell-range'):(
		(TABLENS,u'cell-range-address'),
	),
# allowed_attributes
	(TABLENS,u'source-range-address'):(
		(TABLENS,u'row'),
		(TABLENS,u'table'),
		(TABLENS,u'end-row'),
		(TABLENS,u'end-column'),
		(TABLENS,u'start-table'),
		(TABLENS,u'start-column'),
		(TABLENS,u'column'),
		(TABLENS,u'end-table'),
		(TABLENS,u'start-row'),
	),
# allowed_attributes
	(TABLENS,u'source-service'):(
		(TABLENS,u'user-name'),
		(TABLENS,u'password'),
		(TABLENS,u'name'),
		(TABLENS,u'source-name'),
		(TABLENS,u'object-name'),
	),
# allowed_attributes
	(TABLENS,u'subtotal-field'):(
		(TABLENS,u'function'),
		(TABLENS,u'field-number'),
	),
# allowed_attributes
	(TABLENS,u'subtotal-rule'):(
		(TABLENS,u'group-by-field-number'),
	),
# allowed_attributes
	(TABLENS,u'subtotal-rules'):(
		(TABLENS,u'bind-styles-to-content'),
		(TABLENS,u'case-sensitive'),
		(TABLENS,u'page-breaks-on-group-change'),
	),
# allowed_attributes
	(TABLENS,u'table'):(
		(TABLENS,u'use-first-row-styles'),
		(TABLENS,u'template-name'),
		(TABLENS,u'print-ranges'),
		(TABLENS,u'use-first-column-styles'),
		(TABLENS,u'use-last-row-styles'),
		(TABLENS,u'print'),
		(XMLNS,u'id'),
		(TABLENS,u'is-sub-table'),
		(TABLENS,u'name'),
		(TABLENS,u'use-last-column-styles'),
		(TABLENS,u'protected'),
		(TABLENS,u'use-banding-rows-styles'),
		(TABLENS,u'protection-key'),
		(TABLENS,u'style-name'),
		(TABLENS,u'protection-key-digest-algorithm'),
		(TABLENS,u'use-banding-columns-styles'),
	),
# allowed_attributes
	(TABLENS,u'table-cell'):(
		(XMLNS,u'id'),
		(TABLENS,u'protected'),
		(OFFICENS,u'currency'),
		(TABLENS,u'number-matrix-columns-spanned'),
		(XHTMLNS,u'content'),
		(TABLENS,u'protect'),
		(OFFICENS,u'time-value'),
		(TABLENS,u'number-rows-spanned'),
		(OFFICENS,u'value'),
		(TABLENS,u'formula'),
		(TABLENS,u'style-name'),
		(TABLENS,u'number-columns-spanned'),
		(OFFICENS,u'string-value'),
		(XHTMLNS,u'datatype'),
		(XHTMLNS,u'property'),
		(TABLENS,u'content-validation-name'),
		(OFFICENS,u'date-value'),
		(XHTMLNS,u'about'),
		(OFFICENS,u'value-type'),
		(TABLENS,u'number-matrix-rows-spanned'),
		(OFFICENS,u'boolean-value'),
		(TABLENS,u'number-columns-repeated'),
	),
# allowed_attributes
	(TABLENS,u'table-column'):(
		(TABLENS,u'visibility'),
		(TABLENS,u'style-name'),
		(TABLENS,u'default-cell-style-name'),
		(TABLENS,u'number-columns-repeated'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TABLENS,u'table-column-group'):(
		(TABLENS,u'display'),
	),
# allowed_attributes
	(TABLENS,u'table-columns'):(
	),
# allowed_attributes
	(TABLENS,u'table-header-columns'):(
	),
# allowed_attributes
	(TABLENS,u'table-header-rows'):(
	),
# allowed_attributes
	(TABLENS,u'table-row'):(
		(TABLENS,u'visibility'),
		(TABLENS,u'style-name'),
		(TABLENS,u'number-rows-repeated'),
		(TABLENS,u'default-cell-style-name'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TABLENS,u'table-row-group'):(
		(TABLENS,u'display'),
	),
# allowed_attributes
	(TABLENS,u'table-rows'):(
	),
# allowed_attributes
	(TABLENS,u'table-source'):(
		(XLINKNS,u'type'),
		(TABLENS,u'filter-name'),
		(TABLENS,u'mode'),
		(TABLENS,u'table-name'),
		(XLINKNS,u'href'),
		(TABLENS,u'filter-options'),
		(XLINKNS,u'actuate'),
		(TABLENS,u'refresh-delay'),
	),
# allowed_attributes
	(TABLENS,u'table-template'):(
		(TABLENS,u'last-row-start-column'),
		(TABLENS,u'last-row-end-column'),
		(TABLENS,u'name'),
		(TABLENS,u'first-row-start-column'),
		(TABLENS,u'first-row-end-column'),
	),
# allowed_attributes
	(TABLENS,u'target-range-address'):(
		(TABLENS,u'row'),
		(TABLENS,u'table'),
		(TABLENS,u'end-row'),
		(TABLENS,u'end-column'),
		(TABLENS,u'start-table'),
		(TABLENS,u'start-column'),
		(TABLENS,u'column'),
		(TABLENS,u'end-table'),
		(TABLENS,u'start-row'),
	),
# allowed_attributes
	(TABLENS,u'title'):(
	),
# allowed_attributes
	(TABLENS,u'tracked-changes'):(
		(TABLENS,u'track-changes'),
	),
# allowed_attributes
	(TEXTNS,u'a'):(
		(XLINKNS,u'type'),
		(TEXTNS,u'style-name'),
		(XLINKNS,u'show'),
		(TEXTNS,u'visited-style-name'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(OFFICENS,u'title'),
		(OFFICENS,u'name'),
		(OFFICENS,u'target-frame-name'),
	),
# allowed_attributes
	(TEXTNS,u'alphabetical-index'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'alphabetical-index-auto-mark-file'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
	),
# allowed_attributes
	(TEXTNS,u'alphabetical-index-entry-template'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'alphabetical-index-mark'):(
		(TEXTNS,u'key2'),
		(TEXTNS,u'string-value-phonetic'),
		(TEXTNS,u'key1-phonetic'),
		(TEXTNS,u'key2-phonetic'),
		(TEXTNS,u'main-entry'),
		(TEXTNS,u'string-value'),
		(TEXTNS,u'key1'),
	),
# allowed_attributes
	(TEXTNS,u'alphabetical-index-mark-end'):(
		(TEXTNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'alphabetical-index-mark-start'):(
		(TEXTNS,u'key2'),
		(TEXTNS,u'string-value-phonetic'),
		(TEXTNS,u'key1-phonetic'),
		(TEXTNS,u'key2-phonetic'),
		(TEXTNS,u'main-entry'),
		(TEXTNS,u'id'),
		(TEXTNS,u'key1'),
	),
# allowed_attributes
	(TEXTNS,u'alphabetical-index-source'):(
		(TEXTNS,u'combine-entries-with-pp'),
		(FONS,u'script'),
		(TEXTNS,u'combine-entries'),
		(TEXTNS,u'alphabetical-separators'),
		(TEXTNS,u'main-entry-style-name'),
		(TEXTNS,u'combine-entries-with-dash'),
		(TEXTNS,u'relative-tab-stop-position'),
		(TEXTNS,u'ignore-case'),
		(FONS,u'language'),
		(TEXTNS,u'sort-algorithm'),
		(TEXTNS,u'index-scope'),
		(STYLENS,u'rfc-language-tag'),
		(FONS,u'country'),
		(TEXTNS,u'capitalize-entries'),
		(TEXTNS,u'use-keys-as-entries'),
		(TEXTNS,u'comma-separated'),
	),
# allowed_attributes
	(TEXTNS,u'author-initials'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'author-name'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'bibliography'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'bibliography-configuration'):(
		(FONS,u'script'),
		(FONS,u'language'),
		(TEXTNS,u'prefix'),
		(FONS,u'country'),
		(TEXTNS,u'suffix'),
		(TEXTNS,u'sort-algorithm'),
		(TEXTNS,u'numbered-entries'),
		(STYLENS,u'rfc-language-tag'),
		(TEXTNS,u'sort-by-position'),
	),
# allowed_attributes
	(TEXTNS,u'bibliography-entry-template'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'bibliography-type'),
	),
# allowed_attributes
	(TEXTNS,u'bibliography-mark'):(
		(TEXTNS,u'series'),
		(TEXTNS,u'custom5'),
		(TEXTNS,u'institution'),
		(TEXTNS,u'volume'),
		(TEXTNS,u'report-type'),
		(TEXTNS,u'custom2'),
		(TEXTNS,u'school'),
		(TEXTNS,u'year'),
		(TEXTNS,u'pages'),
		(TEXTNS,u'issn'),
		(TEXTNS,u'bibliography-type'),
		(TEXTNS,u'month'),
		(TEXTNS,u'custom1'),
		(TEXTNS,u'booktitle'),
		(TEXTNS,u'url'),
		(TEXTNS,u'annote'),
		(TEXTNS,u'organizations'),
		(TEXTNS,u'howpublished'),
		(TEXTNS,u'address'),
		(TEXTNS,u'custom3'),
		(TEXTNS,u'chapter'),
		(TEXTNS,u'journal'),
		(TEXTNS,u'custom4'),
		(TEXTNS,u'author'),
		(TEXTNS,u'title'),
		(TEXTNS,u'edition'),
		(TEXTNS,u'identifier'),
		(TEXTNS,u'note'),
		(TEXTNS,u'isbn'),
		(TEXTNS,u'number'),
		(TEXTNS,u'publisher'),
		(TEXTNS,u'editor'),
	),
# allowed_attributes
	(TEXTNS,u'bibliography-source'):(
	),
# allowed_attributes
	(TEXTNS,u'bookmark'):(
		(TEXTNS,u'name'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'bookmark-end'):(
		(TEXTNS,u'name'),
	),
# allowed_attributes
	(TEXTNS,u'bookmark-ref'):(
		(TEXTNS,u'ref-name'),
		(TEXTNS,u'reference-format'),
	),
# allowed_attributes
	(TEXTNS,u'bookmark-start'):(
		(XHTMLNS,u'about'),
		(XMLNS,u'id'),
		(XHTMLNS,u'property'),
		(TEXTNS,u'name'),
		(XHTMLNS,u'content'),
		(XHTMLNS,u'datatype'),
	),
# allowed_attributes
	(TEXTNS,u'change'):(
		(TEXTNS,u'change-id'),
	),
# allowed_attributes
	(TEXTNS,u'change-end'):(
		(TEXTNS,u'change-id'),
	),
# allowed_attributes
	(TEXTNS,u'change-start'):(
		(TEXTNS,u'change-id'),
	),
# allowed_attributes
	(TEXTNS,u'changed-region'):(
		(TEXTNS,u'id'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'chapter'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'display'),
	),
# allowed_attributes
	(TEXTNS,u'conditional-text'):(
		(TEXTNS,u'condition'),
		(TEXTNS,u'current-value'),
		(TEXTNS,u'string-value-if-true'),
		(TEXTNS,u'string-value-if-false'),
	),
# allowed_attributes
	(TEXTNS,u'creation-date'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'date-value'),
	),
# allowed_attributes
	(TEXTNS,u'creation-time'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'time-value'),
	),
# allowed_attributes
	(TEXTNS,u'creator'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'database-display'):(
		(TEXTNS,u'column-name'),
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'table-type'),
		(TEXTNS,u'table-name'),
		(TEXTNS,u'database-name'),
	),
# allowed_attributes
	(TEXTNS,u'database-name'):(
		(TEXTNS,u'table-type'),
		(TEXTNS,u'table-name'),
		(TEXTNS,u'database-name'),
	),
# allowed_attributes
	(TEXTNS,u'database-next'):(
		(TEXTNS,u'condition'),
		(TEXTNS,u'table-type'),
		(TEXTNS,u'table-name'),
		(TEXTNS,u'database-name'),
	),
# allowed_attributes
	(TEXTNS,u'database-row-number'):(
		(STYLENS,u'num-letter-sync'),
		(TEXTNS,u'table-type'),
		(TEXTNS,u'table-name'),
		(STYLENS,u'num-format'),
		(TEXTNS,u'value'),
		(TEXTNS,u'database-name'),
	),
# allowed_attributes
	(TEXTNS,u'database-row-select'):(
		(TEXTNS,u'condition'),
		(TEXTNS,u'table-type'),
		(TEXTNS,u'row-number'),
		(TEXTNS,u'table-name'),
		(TEXTNS,u'database-name'),
	),
# allowed_attributes
	(TEXTNS,u'date'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'date-value'),
		(TEXTNS,u'date-adjust'),
	),
# allowed_attributes
	(TEXTNS,u'dde-connection'):(
		(TEXTNS,u'connection-name'),
	),
# allowed_attributes
	(TEXTNS,u'dde-connection-decl'):(
		(OFFICENS,u'dde-item'),
		(OFFICENS,u'dde-topic'),
		(OFFICENS,u'automatic-update'),
		(OFFICENS,u'dde-application'),
		(OFFICENS,u'name'),
	),
# allowed_attributes
	(TEXTNS,u'dde-connection-decls'):(
	),
# allowed_attributes
	(TEXTNS,u'deletion'):(
	),
# allowed_attributes
	(TEXTNS,u'description'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'editing-cycles'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'editing-duration'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'duration'),
	),
# allowed_attributes
	(TEXTNS,u'execute-macro'):(
		(TEXTNS,u'name'),
	),
# allowed_attributes
	(TEXTNS,u'expression'):(
		(TEXTNS,u'display'),
		(OFFICENS,u'value-type'),
		(OFFICENS,u'value'),
		(OFFICENS,u'date-value'),
		(TEXTNS,u'formula'),
		(OFFICENS,u'currency'),
		(OFFICENS,u'string-value'),
		(STYLENS,u'data-style-name'),
		(OFFICENS,u'boolean-value'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(TEXTNS,u'file-name'):(
		(TEXTNS,u'fixed'),
		(TEXTNS,u'display'),
	),
# allowed_attributes
	(TEXTNS,u'format-change'):(
	),
# allowed_attributes
	(TEXTNS,u'h'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'id'),
		(XMLNS,u'id'),
		(XHTMLNS,u'property'),
		(XHTMLNS,u'about'),
		(TEXTNS,u'start-value'),
		(TEXTNS,u'restart-numbering'),
		(XHTMLNS,u'content'),
		(TEXTNS,u'is-list-header'),
		(XHTMLNS,u'datatype'),
		(TEXTNS,u'cond-style-name'),
		(TEXTNS,u'class-names'),
	),
# allowed_attributes
	(TEXTNS,u'hidden-paragraph'):(
		(TEXTNS,u'condition'),
		(TEXTNS,u'is-hidden'),
	),
# allowed_attributes
	(TEXTNS,u'hidden-text'):(
		(TEXTNS,u'condition'),
		(TEXTNS,u'string-value'),
		(TEXTNS,u'is-hidden'),
	),
# allowed_attributes
	(TEXTNS,u'illustration-index'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'illustration-index-entry-template'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'illustration-index-source'):(
		(TEXTNS,u'caption-sequence-name'),
		(TEXTNS,u'caption-sequence-format'),
		(TEXTNS,u'index-scope'),
		(TEXTNS,u'use-caption'),
		(TEXTNS,u'relative-tab-stop-position'),
	),
# allowed_attributes
	(TEXTNS,u'index-body'):(
	),
# allowed_attributes
	(TEXTNS,u'index-entry-bibliography'):(
		(TEXTNS,u'bibliography-data-field'),
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'index-entry-chapter'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'display'),
	),
# allowed_attributes
	(TEXTNS,u'index-entry-link-end'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'index-entry-link-start'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'index-entry-page-number'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'index-entry-span'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'index-entry-tab-stop'):(
		(STYLENS,u'type'),
		(STYLENS,u'leader-char'),
		(TEXTNS,u'style-name'),
		(STYLENS,u'position'),
	),
# allowed_attributes
	(TEXTNS,u'index-entry-text'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'index-source-style'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'index-source-styles'):(
		(TEXTNS,u'outline-level'),
	),
# allowed_attributes
	(TEXTNS,u'index-title'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'index-title-template'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'initial-creator'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'insertion'):(
	),
# allowed_attributes
	(TEXTNS,u'keywords'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'line-break'):(
	),
# allowed_attributes
	(TEXTNS,u'linenumbering-configuration'):(
		(TEXTNS,u'number-lines'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'restart-on-page'),
		(STYLENS,u'num-letter-sync'),
		(STYLENS,u'num-format'),
		(TEXTNS,u'count-in-text-boxes'),
		(TEXTNS,u'number-position'),
		(TEXTNS,u'offset'),
		(TEXTNS,u'increment'),
		(TEXTNS,u'count-empty-lines'),
	),
# allowed_attributes
	(TEXTNS,u'linenumbering-separator'):(
		(TEXTNS,u'increment'),
	),
# allowed_attributes
	(TEXTNS,u'list'):(
		(TEXTNS,u'continue-list'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'continue-numbering'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'list-header'):(
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'list-item'):(
		(TEXTNS,u'style-override'),
		(TEXTNS,u'start-value'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'list-level-style-bullet'):(
		(STYLENS,u'num-suffix'),
		(TEXTNS,u'bullet-char'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'level'),
		(TEXTNS,u'bullet-relative-size'),
		(STYLENS,u'num-prefix'),
	),
# allowed_attributes
	(TEXTNS,u'list-level-style-image'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(XLINKNS,u'actuate'),
		(XLINKNS,u'show'),
		(TEXTNS,u'level'),
	),
# allowed_attributes
	(TEXTNS,u'list-level-style-number'):(
		(STYLENS,u'num-suffix'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'level'),
		(STYLENS,u'num-letter-sync'),
		(TEXTNS,u'start-value'),
		(STYLENS,u'num-format'),
		(TEXTNS,u'display-levels'),
		(STYLENS,u'num-prefix'),
	),
# allowed_attributes
	(TEXTNS,u'list-style'):(
		(TEXTNS,u'consecutive-numbering'),
		(STYLENS,u'name'),
		(STYLENS,u'display-name'),
	),
# allowed_attributes
	(TEXTNS,u'measure'):(
		(TEXTNS,u'kind'),
	),
# allowed_attributes
	(TEXTNS,u'meta'):(
		(XHTMLNS,u'about'),
		(XHTMLNS,u'content'),
		(XMLNS,u'id'),
		(XHTMLNS,u'property'),
		(XHTMLNS,u'datatype'),
	),
# allowed_attributes
	(TEXTNS,u'meta-field'):(
		(STYLENS,u'data-style-name'),
		(XMLNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'modification-date'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'date-value'),
	),
# allowed_attributes
	(TEXTNS,u'modification-time'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'time-value'),
	),
# allowed_attributes
	(TEXTNS,u'note'):(
		(TEXTNS,u'id'),
		(TEXTNS,u'note-class'),
	),
# allowed_attributes
	(TEXTNS,u'note-body'):(
	),
# allowed_attributes
	(TEXTNS,u'note-citation'):(
		(TEXTNS,u'label'),
	),
# allowed_attributes
	(TEXTNS,u'note-continuation-notice-backward'):(
	),
# allowed_attributes
	(TEXTNS,u'note-continuation-notice-forward'):(
	),
# allowed_attributes
	(TEXTNS,u'note-ref'):(
		(TEXTNS,u'ref-name'),
		(TEXTNS,u'reference-format'),
		(TEXTNS,u'note-class'),
	),
# allowed_attributes
	(TEXTNS,u'notes-configuration'):(
		(STYLENS,u'num-suffix'),
		(TEXTNS,u'note-class'),
		(STYLENS,u'num-letter-sync'),
		(TEXTNS,u'start-value'),
		(TEXTNS,u'master-page-name'),
		(STYLENS,u'num-format'),
		(TEXTNS,u'citation-body-style-name'),
		(TEXTNS,u'start-numbering-at'),
		(TEXTNS,u'footnotes-position'),
		(STYLENS,u'num-prefix'),
		(TEXTNS,u'citation-style-name'),
		(TEXTNS,u'default-style-name'),
	),
# allowed_attributes
	(TEXTNS,u'number'):(
	),
# allowed_attributes
	(TEXTNS,u'numbered-paragraph'):(
		(TEXTNS,u'style-name'),
		(XMLNS,u'id'),
		(TEXTNS,u'level'),
		(TEXTNS,u'start-value'),
		(TEXTNS,u'list-id'),
		(TEXTNS,u'continue-numbering'),
	),
# allowed_attributes
	(TEXTNS,u'object-count'):(
		(STYLENS,u'num-letter-sync'),
		(STYLENS,u'num-format'),
	),
# allowed_attributes
	(TEXTNS,u'object-index'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'object-index-entry-template'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'object-index-source'):(
		(TEXTNS,u'use-other-objects'),
		(TEXTNS,u'relative-tab-stop-position'),
		(TEXTNS,u'use-math-objects'),
		(TEXTNS,u'use-draw-objects'),
		(TEXTNS,u'index-scope'),
		(TEXTNS,u'use-spreadsheet-objects'),
		(TEXTNS,u'use-chart-objects'),
	),
# allowed_attributes
	(TEXTNS,u'outline-level-style'):(
		(STYLENS,u'num-suffix'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'level'),
		(STYLENS,u'num-letter-sync'),
		(TEXTNS,u'start-value'),
		(STYLENS,u'num-format'),
		(TEXTNS,u'display-levels'),
		(STYLENS,u'num-prefix'),
	),
# allowed_attributes
	(TEXTNS,u'outline-style'):(
		(STYLENS,u'name'),
	),
# allowed_attributes
	(TEXTNS,u'p'):(
		(XHTMLNS,u'about'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'id'),
		(XMLNS,u'id'),
		(XHTMLNS,u'property'),
		(XHTMLNS,u'content'),
		(TEXTNS,u'cond-style-name'),
		(XHTMLNS,u'datatype'),
		(TEXTNS,u'class-names'),
	),
# allowed_attributes
	(TEXTNS,u'page'):(
		(TEXTNS,u'master-page-name'),
	),
# allowed_attributes
	(TEXTNS,u'page-continuation'):(
		(TEXTNS,u'string-value'),
		(TEXTNS,u'select-page'),
	),
# allowed_attributes
	(TEXTNS,u'page-number'):(
		(STYLENS,u'num-letter-sync'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'page-adjust'),
		(TEXTNS,u'select-page'),
		(STYLENS,u'num-format'),
	),
# allowed_attributes
	(TEXTNS,u'page-sequence'):(
	),
# allowed_attributes
	(TEXTNS,u'page-variable-get'):(
		(STYLENS,u'num-letter-sync'),
		(STYLENS,u'num-format'),
	),
# allowed_attributes
	(TEXTNS,u'page-variable-set'):(
		(TEXTNS,u'active'),
		(TEXTNS,u'page-adjust'),
	),
# allowed_attributes
	(TEXTNS,u'placeholder'):(
		(TEXTNS,u'placeholder-type'),
		(TEXTNS,u'description'),
	),
# allowed_attributes
	(TEXTNS,u'print-date'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'date-value'),
	),
# allowed_attributes
	(TEXTNS,u'print-time'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'time-value'),
	),
# allowed_attributes
	(TEXTNS,u'printed-by'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'reference-mark'):(
		(TEXTNS,u'name'),
	),
# allowed_attributes
	(TEXTNS,u'reference-mark-end'):(
		(TEXTNS,u'name'),
	),
# allowed_attributes
	(TEXTNS,u'reference-mark-start'):(
		(TEXTNS,u'name'),
	),
# allowed_attributes
	(TEXTNS,u'ruby'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'ruby-base'):(
	),
# allowed_attributes
	(TEXTNS,u'ruby-text'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u's'):(
		(TEXTNS,u'c'),
	),
# allowed_attributes
	(TEXTNS,u'script'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(SCRIPTNS,u'language'),
	),
# allowed_attributes
	(TEXTNS,u'section'):(
		(TEXTNS,u'condition'),
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
		(TEXTNS,u'display'),
	),
# allowed_attributes
	(TEXTNS,u'section-source'):(
		(XLINKNS,u'type'),
		(XLINKNS,u'href'),
		(TEXTNS,u'section-name'),
		(TEXTNS,u'filter-name'),
		(XLINKNS,u'show'),
	),
# allowed_attributes
	(TEXTNS,u'sender-city'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-company'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-country'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-email'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-fax'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-firstname'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-initials'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-lastname'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-phone-private'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-phone-work'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-position'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-postal-code'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-state-or-province'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-street'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sender-title'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'sequence'):(
		(TEXTNS,u'formula'),
		(STYLENS,u'num-letter-sync'),
		(TEXTNS,u'ref-name'),
		(TEXTNS,u'name'),
		(STYLENS,u'num-format'),
	),
# allowed_attributes
	(TEXTNS,u'sequence-decl'):(
		(TEXTNS,u'display-outline-level'),
		(TEXTNS,u'name'),
		(TEXTNS,u'separation-character'),
	),
# allowed_attributes
	(TEXTNS,u'sequence-decls'):(
	),
# allowed_attributes
	(TEXTNS,u'sequence-ref'):(
		(TEXTNS,u'ref-name'),
		(TEXTNS,u'reference-format'),
	),
# allowed_attributes
	(TEXTNS,u'sheet-name'):(
	),
# allowed_attributes
	(TEXTNS,u'soft-page-break'):(
	),
# allowed_attributes
	(TEXTNS,u'sort-key'):(
		(TEXTNS,u'key'),
		(TEXTNS,u'sort-ascending'),
	),
# allowed_attributes
	(TEXTNS,u'span'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'class-names'),
	),
# allowed_attributes
	(TEXTNS,u'subject'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'tab'):(
		(TEXTNS,u'tab-ref'),
	),
# allowed_attributes
	(TEXTNS,u'table-formula'):(
		(TEXTNS,u'formula'),
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'display'),
	),
# allowed_attributes
	(TEXTNS,u'table-index'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'table-index-entry-template'):(
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'table-index-source'):(
		(TEXTNS,u'caption-sequence-name'),
		(TEXTNS,u'caption-sequence-format'),
		(TEXTNS,u'index-scope'),
		(TEXTNS,u'use-caption'),
		(TEXTNS,u'relative-tab-stop-position'),
	),
# allowed_attributes
	(TEXTNS,u'table-of-content'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'table-of-content-entry-template'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'table-of-content-source'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'use-outline-level'),
		(TEXTNS,u'relative-tab-stop-position'),
		(TEXTNS,u'index-scope'),
		(TEXTNS,u'use-index-marks'),
		(TEXTNS,u'use-index-source-styles'),
	),
# allowed_attributes
	(TEXTNS,u'template-name'):(
		(TEXTNS,u'display'),
	),
# allowed_attributes
	(TEXTNS,u'text-input'):(
		(TEXTNS,u'description'),
	),
# allowed_attributes
	(TEXTNS,u'time'):(
		(STYLENS,u'data-style-name'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'time-value'),
		(TEXTNS,u'time-adjust'),
	),
# allowed_attributes
	(TEXTNS,u'title'):(
		(TEXTNS,u'fixed'),
	),
# allowed_attributes
	(TEXTNS,u'toc-mark'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'string-value'),
	),
# allowed_attributes
	(TEXTNS,u'toc-mark-end'):(
		(TEXTNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'toc-mark-start'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'tracked-changes'):(
		(TEXTNS,u'track-changes'),
	),
# allowed_attributes
	(TEXTNS,u'user-defined'):(
		(OFFICENS,u'value'),
		(TEXTNS,u'fixed'),
		(TEXTNS,u'name'),
		(OFFICENS,u'string-value'),
		(STYLENS,u'data-style-name'),
		(OFFICENS,u'boolean-value'),
		(OFFICENS,u'date-value'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(TEXTNS,u'user-field-decl'):(
		(OFFICENS,u'value-type'),
		(OFFICENS,u'value'),
		(OFFICENS,u'date-value'),
		(TEXTNS,u'name'),
		(TEXTNS,u'formula'),
		(OFFICENS,u'currency'),
		(OFFICENS,u'string-value'),
		(OFFICENS,u'boolean-value'),
		(OFFICENS,u'time-value'),
	),
# allowed_attributes
	(TEXTNS,u'user-field-decls'):(
	),
# allowed_attributes
	(TEXTNS,u'user-field-get'):(
		(TEXTNS,u'display'),
		(TEXTNS,u'name'),
		(STYLENS,u'data-style-name'),
	),
# allowed_attributes
	(TEXTNS,u'user-field-input'):(
		(TEXTNS,u'description'),
		(TEXTNS,u'name'),
		(STYLENS,u'data-style-name'),
	),
# allowed_attributes
	(TEXTNS,u'user-index'):(
		(TEXTNS,u'style-name'),
		(TEXTNS,u'protection-key'),
		(XMLNS,u'id'),
		(TEXTNS,u'name'),
		(TEXTNS,u'protected'),
		(TEXTNS,u'protection-key-digest-algorithm'),
	),
# allowed_attributes
	(TEXTNS,u'user-index-entry-template'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'style-name'),
	),
# allowed_attributes
	(TEXTNS,u'user-index-mark'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'string-value'),
		(TEXTNS,u'index-name'),
	),
# allowed_attributes
	(TEXTNS,u'user-index-mark-end'):(
		(TEXTNS,u'id'),
	),
# allowed_attributes
	(TEXTNS,u'user-index-mark-start'):(
		(TEXTNS,u'outline-level'),
		(TEXTNS,u'id'),
		(TEXTNS,u'index-name'),
	),
# allowed_attributes
	(TEXTNS,u'user-index-source'):(
		(TEXTNS,u'use-objects'),
		(TEXTNS,u'copy-outline-levels'),
		(TEXTNS,u'use-index-source-styles'),
		(TEXTNS,u'index-name'),
		(TEXTNS,u'relative-tab-stop-position'),
		(TEXTNS,u'use-floating-frames'),
		(TEXTNS,u'use-graphics'),
		(TEXTNS,u'index-scope'),
		(TEXTNS,u'use-tables'),
		(TEXTNS,u'use-index-marks'),
	),
# allowed_attributes
	(TEXTNS,u'variable-decl'):(
		(TEXTNS,u'name'),
		(OFFICENS,u'value-type'),
	),
# allowed_attributes
	(TEXTNS,u'variable-decls'):(
	),
# allowed_attributes
	(TEXTNS,u'variable-get'):(
		(TEXTNS,u'display'),
		(TEXTNS,u'name'),
		(STYLENS,u'data-style-name'),
	),
# allowed_attributes
	(TEXTNS,u'variable-input'):(
		(TEXTNS,u'description'),
		(TEXTNS,u'display'),
		(TEXTNS,u'name'),
		(OFFICENS,u'value-type'),
		(STYLENS,u'data-style-name'),
	),
# allowed_attributes
	(TEXTNS,u'variable-set'):(
		(TEXTNS,u'display'),
		(OFFICENS,u'value-type'),
		(OFFICENS,u'value'),
		(OFFICENS,u'date-value'),
		(TEXTNS,u'name'),
		(TEXTNS,u'formula'),
		(OFFICENS,u'currency'),
		(OFFICENS,u'string-value'),
		(STYLENS,u'data-style-name'),
		(OFFICENS,u'boolean-value'),
		(OFFICENS,u'time-value'),
	),
}

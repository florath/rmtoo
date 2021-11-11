;;
;;
;; rmtoo
;;   Free and Open Source Requirements Management Tool
;;
;; Emacs Mode for editing requirments
;;
;; (c) 2010-2011 by flonatel
;;
;; For licencing details see COPYING
;;

(defconst req-tags-plain
  '("Name" "Type" "Invented on" "Invented by"
    "Depends on"
    "Solved by" "History" "Owner" "Description" "Status"
    "Rationale" "Class" "Priority" "Note" "Effort estimation"
    "Topic")
  "List of strings with known REQ types.")

;; Tags must be at the beginning of line, ending with a colon.
(defconst req-tags-opt
  (concat
   '"^"
   (regexp-opt req-tags-plain)
   '":"))

(defgroup req-mode nil
  "REQ master file mode configuration."
  :group 'data)

(defconst req-mode-classes 
  '("master requirement" "design decision" 
    "initial requirement" "requirement")
  "List of strings with known REQ classes.")

;; Font lock.
(defvar req-mode-type-face 'font-lock-type-face
  "Name of face used for REQ tags (Name:).")

(defvar req-mode-class-face 'font-lock-constant-face
  "Name of face used for REQ classes (requirement).")

(defcustom req-mode-font-lock-keywords
  `((,(regexp-opt req-mode-classes) 0 ,req-mode-class-face)
    (,req-tags-opt 0 ,req-mode-type-face))
  "Font lock keywords used to highlight text in REQ mode."
  :type 'sexp
  :group 'req-mode)

;; Syntax table.
(defvar req-mode-syntax-table
  (let ((table (make-syntax-table)))
    (modify-syntax-entry ?\# "<   " table)
    (modify-syntax-entry ?\n ">   " table)
    table)
  "Syntax table in use in REQ buffers.")

(defvar req-mode-menu nil
  "Menubar used in REQ mode.")

;;; Indentation
;;; (loosly based on the sample major mode coming with emacs)
(defun req-indent-line ()
  "Indent current line of requirment."
  (interactive)
  (let ((savep (> (current-column) (current-indentation)))
	(indent (condition-case nil (max (req-calculate-indentation) 0)
		  (error 0))))
    (if savep
	(save-excursion (indent-line-to indent))
      (indent-line-to indent))))

(defun req-calculate-indentation ()
  "Return the column to which the current line should be indented."
  (or
   ;; Stick the first line at column 0.
   (and (= (point-min) (line-beginning-position)) 0)
   ;; Keywords start at column 0.
   (and (looking-at req-tags-opt) 0)
   ;; One is the one for normal lines (which are part of a block for
   ;; the key). 
   1))

;;;###autoload
(define-derived-mode req-mode text-mode "REQ"
  "Major mode for viewing and editing requirment files."
  (set (make-local-variable 'font-lock-defaults)
       '(req-mode-font-lock-keywords nil nil ((?_ . "w"))))
  (set (make-local-variable 'comment-start) "# ")
  (set (make-local-variable 'comment-start-skip) "#+\\s-*")
  (set (make-local-variable 'indent-line-function) 'req-indent-line)
  ;; Just write the requirments
  (auto-fill-mode)
  ;; Mostly all is plain text
  (flyspell-mode))

;;;###autoload
(add-to-list 'auto-mode-alist '("\\.req\\'" . req-mode))

(provide 'req-mode)

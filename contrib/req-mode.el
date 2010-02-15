;;
;; Requirement Management Toolset
;;
;;   Emacs Mode for editing requirments
;;
;; (c) 2010 by flonatel
;;
;; For licencing details see COPYING
;;

(defconst req-tags-plain
  '("Name" "Type" "Invented on" "Invented by"
    "Depends on" "History" "Owner" "Description" "Status"
    "Rationale" "Class")
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
    (modify-syntax-entry ?\; "<   " table)
    (modify-syntax-entry ?\n ">   " table)
    table)
  "Syntax table in use in REQ buffers.")

(defvar req-mode-menu nil
  "Menubar used in REQ mode.")

;;;###autoload
(define-derived-mode req-mode text-mode "REQ"
  "Major mode for viewing and editing requirment files."
  (set (make-local-variable 'font-lock-defaults)
       '(req-mode-font-lock-keywords nil nil ((?_ . "w")))))

;;;###autoload
(add-to-list 'auto-mode-alist '("\\.req\\'" . req-mode))

(provide 'req-mode)

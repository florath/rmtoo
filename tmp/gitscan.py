#
# Tests for using python git
#

import git

def main():
    repo = git.Repo(".")
    print(repo)

    print(repo.commits())

    head = repo.commits()[0]
    print("HEAD %s" % head)

    print("DIR Commit '%s'" % dir(head))

    diffs = head.diff(repo, head.id)
    print("Commit diff '%s'" % diffs)

    for d in diffs:
        print("DIR diff '%s'" % dir(d))
        print("DIFF '%s'" % d.diff)
        print("a_commit '%s'" % d.a_commit)
        print("b_commit '%s'" % d.b_commit)
        print("a_path '%s'" % d.a_path)
        print("b_path '%s'" % d.b_path)

    parents = head.parents
    print("Parents %s" % parents)

    tree = head.tree
    print("Tree %s" % tree)

    author = head.author
    print("Author '%s'" % author)

    message = head.message
    print("Message '%s'" % message)
    
    items = tree.items()
    print("Contents '%s'" % items)

    # doc/requirement

    reqdir_tree = tree/"doc"/"requirements"
    print("ReqDir contents '%s'" % (reqdir_tree))

    reqdir_items = reqdir_tree.items()
    print("ReqDir Contents '%s'" % reqdir_items)

    # doc/requirement/TestBeforePack.req

    tbp_file = reqdir_tree["TestBeforePack.req"]
    print("TestBeforePack file %s" % tbp_file)

    print("DATA: '%s'" % tbp_file.data)

    print("DDDDDDDDIIIIIIIIIIIIIIIIFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")

    diffs = git.Diff.list_from_string(repo, "doc/requirements")
    print("DIFFS '%s'" % diffs)


if __name__=="__main__":
    main()

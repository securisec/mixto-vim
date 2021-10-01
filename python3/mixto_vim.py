from mixto import MixtoLite
import vim
import os

m = MixtoLite()

def _get_ids():
    try:
        return vim.command("let s:mixto_entry_ids = %s" % m.GetEntryIDs())
    except Exception as e:
        print('Could not connect to the Mixto server')

def mixto_commit():
    try:
        # get entry id from argument
        entry_id = vim.eval("a:entryID")
        buffer = vim.current.buffer

        buffer_content = []
        file_name = os.path.basename(buffer.name)
        title = file_name if file_name else "Untitled buffer"

        # read buffer line by line
        for line in range(len(buffer)):
            buffer_content.append(buffer[line])

        # if buffer is empty, return
        if len(buffer_content) == 0:
            print("Buffer is empty, nothing to commit")
            return
        buffer_content = "\n".join(buffer_content)

        m.AddCommit(buffer_content, entry_id, f'(Vim) {title}')
        print("Added commit to Mixto")
    except:
        print("Error while committing buffer")

---
name: everything-cli
compatibility: Windows only. Requires the official Everything desktop app and ES (`es.exe`); Everything must be running.
description: >
  Use on Windows when a file, directory, or project may be outside the known
  working directory or its location is unclear, especially with OneDrive Files
  On-Demand. Locate it through Everything's filename and path index before
  recursive filesystem search. Do not use for content search inside an already
  known directory.
---

# Everything CLI

Use `es.exe` as a locator. It searches Everything's existing filename and path
index; it does not replace local code search.

## Locate the target

1. Start with a filename fragment and return full paths with a small result
   limit:

   ```powershell
   es.exe -n 20 -full-path-and-name filename-fragment
   ```

   If `es.exe` fails, report that the official Everything desktop app and ES are
   required. When the target root is already known, continue with local tools;
   otherwise, do not replace ES with a broad recursive scan.

   To combine filename and project or directory clues, match the full path and
   pass each fragment as a separate argument:

   ```powershell
   es.exe -n 20 -p -full-path-and-name project-fragment filename-fragment
   ```

   ES combines separate fragments with AND. Quote or escape each fragment as
   required by PowerShell and ES, including fragments with spaces or special
   characters. Use `/ad` for directories, `/a-d` for files, or
   `-path "C:\known\root"` when the task already limits the search to a particular
   root.

2. Use the returned paths and task context to identify the intended result.
   Once its directory is known, switch to the normal local tools for any
   structure or content search, keeping those tools within that directory.

## Keep discovery index-only

- Search names and paths, not file contents. Avoid `content:` and properties
  that are not known to be indexed because they may read cloud-only files.
- Do not use drive-wide `rg`, `grep`, globbing, or directory traversal as a
  fallback while the target root is unknown.
- Respect the active task's access boundaries even when Everything exposes a
  wider index.
- Treat results as an indexed view. If a query misses, simplify or reformulate
  its fragments first; the location may also be excluded or the index stale.

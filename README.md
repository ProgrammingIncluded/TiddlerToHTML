# Tiddler to HTML
Python to converts eachtiddler files (.tid) in a folder into
the corresponding HTML file in another folder.

## Usage

```
python tparse <foldername> <outputfolder>
```

## Remarks
Currently the project does not have very thorough parsing.
The project was designed for easy, quick, and dirty solution
for an internal project. Mass majority .tid files are markdown.

The metadata on each .tid file is appended at the beginning
of each HTML file. You can use it to parse metadata or
remove them entirely.
# -*- coding: utf-8 -*-
"""
df2latex

Create latex \booktabs formatted table from pandas dataframe. Table files can
be included in another .tex file using the \input command.

df2latex.convert returns list of lines for latex formatted table and
optionally writes table to file. You can specify column format using

    Inputs:

    write_name: name of file [default = False (no file written)]

    just: column justification/width [default = '']

    sz = font size [default = '\\small']

df2latex.write_file() provides a method to easily write lists to files. Useful
if combining multiple tables

Created on Fri Apr 24 13:41:42 2015

@author: Daniel Marasco

"""


#Convert to list of Latex Rows
def convert(df,name = '',write_name = False, just = '', sz = '\\small'):

    # Create empty table list
    latex = []

    # Create table header from df.columns
    line = ' & '.join(df.columns) + r' \\'

    # Create top of table
    latex.extend([
                  '\\begin{table}[H]',sz,
                  '\\caption {%s}' % name,
                  '\\begin{tabular}%s' % just,
                  '\\toprule', line, '\\midrule'])

    # Add all DataFrame rows to table
    latex.extend(df.apply(lambda x: ' & '.join(x.astype(str))+r' \\',axis=1))

    # Add bottom format information
    latex.extend(['\\bottomrule', '\\end{tabular}', '\\end{table}'])

    # Write file
    if bool(write_name):
        write_file(latex, write_name)

    return latex


# Output using write()
def write_file(latex,file_name = 'df_to_latex.tex'):

    f = file(file_name,'w')

    for line in latex:
        f.write(line + '\n')
    f.close()

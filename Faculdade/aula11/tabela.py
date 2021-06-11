
from docx import Document
from docx.shared import Inches

doc = Document()

tab = doc.add_table(rows=1, cols=2)
tab.style="Medium Grid 3 Accent 4"
cels = tab.rows[0].cells
cels[0].text = 'Prioridade'
cels[1].text = "Tarefas"

# Três tarefas importantes das pessoas em uma tabela
for numero in range(1, 4):
   dados = tab.add_row().cells
   tarefa = input("Qual é a tarefa de prioridade número-{}? ".format(numero))
   dados[0].text = str(numero)
   dados[1].text = tarefa

doc.save('f:\\z.doc\\meudoc.docx')


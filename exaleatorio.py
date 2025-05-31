import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Configurações do tempo
total_time = 26
tasks = {
  "Tarefa 1": {"computation": 1, "period": 4, "deadline": 4},
  "Tarefa 2": {"computation": 2, "period": 6, "deadline": 6},
  "Tarefa 3": {"computation": 3, "period": 10, "deadline": 7},
}

# Inicializando a lista de eventos
events = []

# Gerando eventos para cada tarefa
for task_name, task in tasks.items():
  computation = task['computation']
  period = task['period']
  
  for start_time in range(0, total_time + period, period):
    if start_time + computation <= total_time:
      events.append((start_time, start_time + computation, task_name))

# Criando o gráfico
fig, ax = plt.subplots(figsize=(12, 4))

# Adicionando as tarefas ao gráfico
for start, end, task_name in events:
  color = 'red' if task_name == "Tarefa 1" else 'gray' if task_name == "Tarefa 2" else 'green'
  ax.add_patch(mpatches.Rectangle((start, 0), end - start, 1, color=color, label=task_name))

# Configurações do gráfico
ax.set_xlim(0, total_time)
ax.set_ylim(0, 1)
ax.set_yticks([])
ax.set_xticks(range(0, total_time + 1))
ax.set_xticklabels(range(0, total_time + 1))

# Criando uma legenda única
handles = [mpatches.Patch(color='red', label='Tarefa 1'),
          mpatches.Patch(color='gray', label='Tarefa 2'),
          mpatches.Patch(color='green', label='Tarefa 3')]

plt.title("Diagrama de Escalonamento das Tarefas")
plt.xlabel("Tempo")
plt.legend(handles=handles, loc='upper right')

# Exibindo o gráfico
plt.grid()
plt.show()
import React, { useState } from 'react';
import { View, Text, FlatList, TouchableOpacity, Modal, TextInput, Button as RNButton, Switch, StyleSheet } from 'react-native';

type Task = {
  id: string;
  text: string;
  completed: boolean;
};

const App = () => {
  const [tasks, setTasks] = useState<Task[]>([
    { id: '1', text: 'Estudar TSX', completed: false },
    { id: '2', text: 'Estudar React', completed: true },
    { id: '3', text: 'Terminar projeto', completed: false },
  ]);
  const [isModalVisible, setModalVisible] = useState<boolean>(false);
  const [newTaskText, setNewTaskText] = useState<string>('');

  const toggleTaskStatus = (taskId: string) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === taskId ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const addNewTask = () => {
    if (newTaskText.trim() !== '') {
      setTasks((prevTasks) => [
        ...prevTasks,
        { id: (prevTasks.length + 1).toString(), text: newTaskText, completed: false },
      ]);
    }
    setModalVisible(false);
    setNewTaskText('');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Lista de Tarefas</Text>
      
      <FlatList
        data={tasks}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.taskItem}>
            <Text style={styles.taskText}>{item.text}</Text>
            <View style={styles.taskStatus}>
              <Switch
                value={item.completed}
                onValueChange={() => toggleTaskStatus(item.id)}
              />
              <Text style={item.completed ? styles.completed : styles.pending}>
                {item.completed ? 'Concluída' : 'Pendente'}
              </Text>
            </View>
          </View>
        )}
      />

      <TouchableOpacity onPress={() => setModalVisible(true)} style={styles.addButton}>
        <Text style={styles.addButtonText}>Adicionar Tarefa</Text>
      </TouchableOpacity>

      <Modal visible={isModalVisible} animationType="slide">
        <View style={styles.modalContainer}>
          <Text style={styles.modalTitle}>Nova Tarefa</Text>
          <TextInput
            placeholder="Digite a nova tarefa"
            style={styles.input}
            onChangeText={(text) => setNewTaskText(text)}
            value={newTaskText}
          />
          <View style={styles.modalButtons}>
            <RNButton title="Adicionar" onPress={addNewTask} color="blue" />
            <RNButton title="Cancelar" onPress={() => setModalVisible(false)} color="orange" />
          </View>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: "#fff",
  },
  title: {
    fontSize: 20,
    marginBottom: 20,
    marginTop: 20,
    fontWeight: "bold",
  },
  taskItem: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 10,
    padding: 10,
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 5,
  },
  taskText: {
    fontSize: 16,
  },
  taskStatus: {
    flexDirection: "row",
    alignItems: "center",
  },
  completed: {
    color: "green",
    marginLeft: 10,
  },
  pending: {
    color: "red",
    marginLeft: 10,
  },
  addButtonText: {
    color: "white",
    fontSize: 16,
  },
  addButton: {
    backgroundColor: "blue",
    padding: 10,
    borderRadius: 5,
  },
  modalContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  modalTitle: {
    fontSize: 20,
    marginBottom: 20,
  },
  input: {
    borderColor: "gray",
    borderWidth: 1,
    padding: 10,
    width: "80%",
    marginBottom: 10,
  },
  modalButtons: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: "80%",
  },
});

export default App;
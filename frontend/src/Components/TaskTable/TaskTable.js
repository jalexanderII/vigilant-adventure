import { List } from "@mui/material";
import Container from "@mui/material/Container";
import Task from "../Task/Task";
import { useEffect, useState } from "react";


function TaskTable() {
  const [tasks, setTasks] = useState([]);

  const getTasks = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/tasks/joel');

      if (!res.ok) {
        const message = `An error has occured: ${res.status} - ${res.statusText}`;
        throw new Error(message);
      }

      const data = await res.json();
      console.log(data)
      const loadedTasks = []

      for (const task in data){
        loadedTasks.push(task)
      }

      setTasks(loadedTasks);
    } catch (err) {
      throw new Error(err.message);
    }
  }

  useEffect(() => {
    return () => {
      getTasks();
    };
  }, []);

  return (
    <Container sx={{ bgcolor: "#cfb8fc", height: "100vh" }}>
      <List sx={{ width: "100%", bgcolor: "background.paper" }}>
        {tasks.map((value) => {
          const labelId = `checkbox-list-label-${value}`;
          return <Task value={value} labelId={labelId} />;
        })}
      </List>
    </Container>
  );
}

export default TaskTable;

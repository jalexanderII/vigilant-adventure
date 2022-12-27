import { List } from "@mui/material";
import Container from "@mui/material/Container";
import Task from "../Task/Task";

const Task1 = {
  content: "This is a task",
  completed: false,
  username: "John",
  created_at: new Date(),
  completed_at: null,
  priority: "normal",
};
const Task2 = {
  content: "This is 2 tasks",
  completed: false,
  username: "John",
  created_at: new Date(),
  completed_at: null,
  priority: "normal",
};
const Task3 = {
  content: "This is 3 tasks",
  completed: false,
  username: "John",
  created_at: new Date(),
  completed_at: null,
  priority: "urgent",
};
const Task4 = {
  content: "This is 4 tasks",
  completed: false,
  username: "John",
  created_at: new Date(),
  completed_at: null,
  priority: "urgent",
};

const ListItems = [Task1, Task2, Task3, Task4];

function TaskTable() {
  return (
    <Container sx={{ bgcolor: "#cfb8fc", height: "100vh" }}>
      <List sx={{ width: "100%", bgcolor: "background.paper" }}>
        {ListItems.map((value) => {
          const labelId = `checkbox-list-label-${value}`;
          return <Task value={value} labelId={labelId} />;
        })}
      </List>
    </Container>
  );
}

export default TaskTable;

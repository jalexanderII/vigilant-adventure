import Container from '@mui/material/Container';
import Task from '../Task/Task';
function TaskTable() {
    return (
     <Container sx={{ bgcolor: '#cfb8fc', height: '100vh' }}>
        <Task />
        </Container>

    ) 
}

export default TaskTable;
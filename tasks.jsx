import { useReducer, useState } from "react";


//initial state
const initialState = [];

//Reducer function
const tasksReducer = (state, action) => {
  switch (action.type) {
    case "ADD_TASK":
      return [...state,{ id: Date.now(), text: action.payload}];
    case 'UPDATE_TASK':
        return state.map((task) =>
          task.id === action.payload.id ? { ...task, text: action.payload.text } : task
        );
    case 'DELETE_TASK':
        return state.filter((task) => task.id !== action.payload);
    default:
      return state;
  }
};

const NewTasks = () => {
    const [tasks, dispatch] = useReducer(tasksReducer, initialState); 
    const[taskText, setTaskText] = useState('');
    const[editTask, setEditTask] = useState(null);

    const handleAddTask = () => {
        if(taskText.trim()){
            dispatch({type: 'ADD_TASK', payload: taskText});
            setTaskText('');
        }
    };

    const handleUpdateTask = () => {
        if (editTask && taskText.trim()) {
          dispatch({ type: 'UPDATE_TASK', payload: { id: editTask.id, text: taskText } });
          setEditTask(null);
          setTaskText('');
        }
    };

    const handleEdit = task => {
        setEditTask(task);
        setTaskText(task.text);
    };

    const handleDelete = id => {
        dispatch({ type: 'DELETE_TASK', payload: id });
    };
    return (
        <div>
            <h1>Task Manager</h1>
            <div>
                <input type='text' value={taskText} onChange={e => setTaskText(e.target.value)}  placeholder="Enter Task" />

                {editTask ? (
                    <button onClick={handleUpdateTask}>Update Task</button>
                ) : (
                    <button onClick={handleAddTask}>Add Task</button>
                )}
            </div>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        {task.text}
                        <button onClick={() => handleEdit(task)}>Edit</button>
                        <button onClick={() => handleDelete(task.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    )
    }

    export default NewTasks;


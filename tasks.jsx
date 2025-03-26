

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
        return state.filter((task) => task.id !== action.payload.id);
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
    }

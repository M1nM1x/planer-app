import LoginForm from "./components/LoginForm.jsx";
import axios from "axios";
import {useEffect} from "react";

function App() {

    const fetchUsers = () => {
        axios.get('http://localhost:8000/api/v1/users').then(response => {
            console.log('response', response)
        })
    }

    useEffect(() => {
        fetchUsers()
    }, [])

    return (
        <>
          <LoginForm />
        </>
      )
}

export default App

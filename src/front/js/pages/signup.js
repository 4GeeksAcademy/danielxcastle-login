import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";

export const SignUp = () => {
    const { store, actions } = useContext(Context)
    const [ email, setEmail ] = useState("");
    const [ password, setPassword ] = useState("");
    const onSubmit = (event) => {
		actions.signUp({
			email: email,
			password: password
		});
		navigate("/");
	};
    return (
        <div className="container">
            <h1>Sign up below!</h1>
            <input 
                className="form-control m-3" 
                type="email" value={email} 
                placeholder="email"
                onChange={(event) => setEmail(event.target.value)}
                ></input>
            <input 
                className="form-control m-3" 
                type="password" value={password} 
                placeholder="password"
                onChange={(event) => setPassword(event.target.value)}
                ></input>
            <button className="btn btn-success" onClick={onSubmit}>Submit</button>

        </div>
    )
}
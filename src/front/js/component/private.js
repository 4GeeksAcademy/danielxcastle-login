import React, { useContext } from "react";
import { Context } from "../store/appContext";

export const Private = () => {
    const { store, actions } = useContext(Context)
    return (
        <div className="container">
            <h1></h1>

        </div>

    )
}
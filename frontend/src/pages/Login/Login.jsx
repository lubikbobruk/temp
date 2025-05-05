import { useState } from "react"

import s from "./Login.module.css"
import g from "../../App.module.css"
import Input from "../../components/Input/Input"
import Button from "../../components/Button/Button"
import axios from "../../api/axios"

const Login = () => {
  const [formValues, setFormValues] = useState({
    login: "",
    password: "",
  })
  const [error, setError] = useState({})

  const inputOnChange = (e) => {
    setFormValues({ ...formValues, [e.target.name]: e.target.value })
  }

  const inputs = [
    {
      id: 0,
      name: "login",
      type: "text",
      placeholder: "Login",
      label: "Login",
      errorMessage:
        "Username must contain 6-20 characters (uppercase, lowercase or numbers)",
      pattern: "^[A-Za-z0-9]{6,20}$",
      required: true,
    },
    {
      id: 1,
      name: "password",
      type: "password",
      placeholder: "Password",
      label: "Password",
      errorMessage: "Password must contain 6-20 characters",
      pattern: "^.{6,20}$",
      required: true,
    },
  ]

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (validateForm()) {
      try {
        const response = await axios.post(
          "/register",
          JSON.stringify(...formValues),
          {
            headers: {
              "Content-Type": "application/json",
            },
            withCredentials: true,
          }
        )
        console.log(response.data)
        console.log(response.accessToken)
      } catch (err) {}
    }
  }

  const validateForm = () => {
    const errors = {}

    inputs.forEach((input) => {
      if (input.required && !formValues[input.name]) {
        errors[input.name] = `${input.label} is required`
      } else if (
        input.pattern &&
        !new RegExp(input.pattern).test(formValues[input.name])
      ) {
        errors[input.name] = input.errorMessage
      }
    })

    setError(errors)
    return Object.keys(errors).length === 0
  }

  return (
    <>
      <div className={s.Login}>
        <div className={g.container}>
          <div className={s.loginContainer}>
            <form onSubmit={handleSubmit}>
              <div className={s.formWrapper}>
                <div className={s.formTitle}>Hi, friend. Please, log in</div>
                {inputs.map((input) => (
                  <div key={input.id} className={s.inputWrapper}>
                    <Input
                      name={input.name}
                      placeholder={input.placeholder}
                      value={formValues[input.name]}
                      type={input.type}
                      onChange={inputOnChange}
                      errorMessage={error[input.name]}
                      valid={!error[input.name]}
                    />
                  </div>
                ))}
                <div className={s.buttonWrapper}>
                  <Button>Log in</Button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  )
}

export default Login

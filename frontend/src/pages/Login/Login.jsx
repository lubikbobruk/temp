import { useState } from "react"
import { useNavigate } from "react-router-dom";
import s from "./Login.module.css"
import g from "../../App.module.css"
import Input from "../../components/Input/Input"
//import Button from "../../components/Button/Button"
import axios from "../../api/axios"


const Button = ({ children, ...rest }) => {
  return (
    <button className={s.Button} {...rest}>
      {children}
    </button>
  )
}


const Login = () => {
  const [formValues, setFormValues] = useState({
    user_email: "",
    user_password: "",
  })
  const [error, setError] = useState({})
  const navigate = useNavigate();

  const inputOnChange = (e) => {
    setFormValues({ ...formValues, [e.target.name]: e.target.value })
  }

  const inputs = [
    {
      id: 0,
      name: "user_email",
      type: "email",
      placeholder: "Email",
      label: "Email",
      errorMessage:
        "Enter a valid email address",
      pattern: "^[\\w-.]+@([\\w-]+\\.)+[\\w-]{2,4}$",
      required: true,
    },
    {
      id: 1,
      name: "user_password",
      type: "password",
      placeholder: "Password",
      label: "Password",
      errorMessage: "Password is required",
      pattern: "^.{1,20}$",
      required: true,
    },
  ]

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (validateForm()) {
      try {
        const response = await axios.post(
          "/auth/login",
          JSON.stringify(formValues),
          {
            headers: { "Content-Type": "application/json" },
            withCredentials: true
          }
        )
        console.log(response.data)
        console.log(response.accessToken)
        localStorage.setItem("token", response.data.accessToken)
        navigate("/films")
      } catch (err) {
        console.error(err.response?.data?.message || "Login failed")
      }
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
      <div 
        className={s.Login}
        style = {{
          backgroundImage: `url("/assets/library.jpg")`,
        }}
      >
        <div className={g.container}>
          <div className={s.loginContainer}>
            <form onSubmit={handleSubmit}>
              <div className={s.formWrapper}>
                <div className={s.formTitle}>The Book Portal</div>
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
                      //className={s.formInput}
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

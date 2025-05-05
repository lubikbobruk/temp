import { useState } from "react"
import s from "./Input.module.css"

const Input = (props) => {
  const { errorMessage, valid, name, ...inputProps } = props
  const inputClass = valid ? "" : s.invalidInput

  const [focus, setFocus] = useState(false)

  return (
    <>
      <input
        className={`${s.Input} ${inputClass}`}
        {...inputProps}
        name={name}
      />
      {errorMessage && <span>{errorMessage}</span>}
    </>
  )
}

export default Input

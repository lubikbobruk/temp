import s from "./Button.module.css"

const Button = ({ children, ...rest }) => {
  return (
    <button className={s.Button} {...rest}>
      {children}
    </button>
  )
}

export default Button

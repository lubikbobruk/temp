import Button from "../Button/Button"
import s from "./CommentField.module.css"

const CommentField = () => {
  return (
    <div>
      <textarea
        className={s.CommentField}
        placeholder='Type a comment...'
      ></textarea>
      <div className={s.buttonContainer}>
        <Button>Post</Button>
      </div>
    </div>
  )
}

export default CommentField

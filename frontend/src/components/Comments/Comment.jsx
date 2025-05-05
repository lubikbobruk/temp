import s from './Comment.module.css'

import  {FaUserCircle} from 'react-icons/fa'

const Comment = () => {
  return (
    <div className={s.Comment}>
      <div className={s.profileContainer}>
        <FaUserCircle alt='Profile icon' size={50} style={{display: 'block'}}/>
        <div className={s.nickname}>
          boro boro
        </div>
      </div>
      <div className={s.comment}>я ебал этот фильм пиздец </div>
    </div>
  )
}

export default Comment
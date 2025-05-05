import s from "./PageWrapper.module.css"
import g from "../../App.module.css"
import Header from "../../components/Header/Header"


const PageWrapper = ({ children }) => {
  return (
    <>
      <div className={s.PageWrapper}>
        <div className={g.container}>
          <Header />
          {children}
        </div>
      </div>
    </>
  )
}

export default PageWrapper

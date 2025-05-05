import { useState } from "react"

import s from "./Header.module.css"
import g from "../../App.module.css"
import equipment from "../../res/icons/equipment.svg"
import logo from "../../res/icons/logo.jpg"
import Button from "../Button/Button"
import { Link, useLocation } from "react-router-dom"

const navigation = [{ alt: "Home", icon: equipment, link: "/films" }]

const Header = () => {
  const path = "/" + useLocation().pathname.split("/")[1]

  return (
    <div className={s.Header}>
      <div className={s.headerContainer}>
        <div className={s.iconColumn}>
          {navigation.map((nav, index) => (
            <div key={index} className={s.icon}>
              <Link to={nav.link}>
                <img
                  className={path === nav.link ? s.active : ""}
                  src={nav.icon}
                  alt={nav.alt}
                />
              </Link>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Header

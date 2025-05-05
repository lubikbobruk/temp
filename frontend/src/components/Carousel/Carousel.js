import { useState } from "react"
import ReactSimplyCarousel from "react-simply-carousel"
import { MdOutlineKeyboardArrowRight } from "react-icons/md"
import { MdOutlineKeyboardArrowLeft } from "react-icons/md"

const Carousel = ({ children }) => {
  const [activeSlideIndex, setActiveSlideIndex] = useState(0)

  return (
    <ReactSimplyCarousel
      infinite={false}
      activeSlideIndex={activeSlideIndex}
      onRequestChange={setActiveSlideIndex}
      innerProps={{
        style: {
          height: 500,
          display: "flex",
          alignItems: "center",
        },
      }}
      forwardBtnProps={{
        //here you can also pass className, or any other button element attributes
        style: {
          alignSelf: "center",
          background: "#31A3EC",
          border: "none",
          borderRadius: "50%",
          color: "white",
          cursor: "pointer",
          height: 50,
          width: 50,
          lineHeight: 1,
        },
        children: <MdOutlineKeyboardArrowRight size={30} alt='Arrow left' />,
      }}
      backwardBtnProps={{
        //here you can also pass className, or any other button element attributes
        style: {
          alignSelf: "center",
          background: "#31A3EC",
          border: "none",
          borderRadius: "50%",
          color: "white",
          cursor: "pointer",
          height: 50,
          width: 50,
          lineHeight: 1,
        },
        children: <MdOutlineKeyboardArrowLeft size={30} alt='Arrow right' />,
      }}
      speed={500}
      easing='linear'
    >
      {children}
    </ReactSimplyCarousel>
  )
}

export default Carousel

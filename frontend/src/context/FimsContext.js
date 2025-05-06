import { createContext } from "react"

const FilmsContext = createContext()

const films = [
  {
    id: 101,
    title: "The Hunger Games",
    image: "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
  },
  {
    id: 102,
    title: "Harry Potter and the Philosopher's Stone",
    image: "https://m.media-amazon.com/images/I/51UoqRAxwEL._SY445_SX342_.jpg",
  },
  {
    id: 103,
    title: "Pride and Prejudice",
    image: "https://m.media-amazon.com/images/I/51Z0nLAfLmL.jpg",
  },
  {
    id: 104,
    title: "The Hobbit",
    image: "https://m.media-amazon.com/images/I/41aQPTCmeVL._SY445_SX342_.jpg",
  },
  {
    id: 105,
    title: "The Great Gatsby",
    image: "https://upload.wikimedia.org/wikipedia/commons/7/7a/The_Great_Gatsby_Cover_1925_Retouched.jpg",
  },
  {
    id: 106,
    title: "To Kill a Mockingbird",
    image: "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657.jpg",
  },
  {
    id: 107,
    title: "The Catcher in the Rye",
    image: "https://cdn.knihcentrum.cz/98805129_the-catcher-in-the-rye-1.jpg",
  },
  {
    id: 108,
    title: "1984",
    image: "https://data.knizniklub.cz/book/015/858/0158581/large.jpg",
  },
  {
    id: 109,
    title: "The Lord of the Rings",
    image: "https://m.media-amazon.com/images/I/51EstVXM1UL._SY445_SX342_.jpg",
  },
  {
    id: 110,
    title: "The Design of Everyday Things",
    image: "https://m.media-amazon.com/images/I/81zpLhP1gWL.jpg",
  },
]

export const FilmsProvider = ({ children }) => {
  return (
    <FilmsContext.Provider value={{ films }}>
      {children}
    </FilmsContext.Provider>
  )
}

export default FilmsContext

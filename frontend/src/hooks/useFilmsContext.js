import { useContext } from "react";
import FilmsContext from "../context/FimsContext";


export default function useFilmsContext() {
  return useContext(FilmsContext)
}
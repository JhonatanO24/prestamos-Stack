import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

export async function getLibros() {
  const res = await API.get("/libros");
  return res.data;
}

export async function crearPrestamo(payload) {
  const res = await API.post("/prestamos/", payload);
  return res.data;
}

export async function devolverPrestamo(prestamoId) {
  const res = await API.put(`/prestamos/devolucion/${prestamoId}`);
  return res.data;
}

export async function getPrestamos() {
    const res = await API.get("/prestamos");
    return res.data;
}
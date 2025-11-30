import React, { useEffect, useState } from "react";
import { getLibros, getPrestamos, crearPrestamo, devolverPrestamo } from "../api.js"; 
import BookList from "../components/BookList.jsx"; 
import PrestamoList from "../components/PrestamoList.jsx"; 
import toast from "react-hot-toast"; 

export default function Home() {
  const [libros, setLibros] = useState([]);
  const [prestamos, setPrestamos] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchLibros = async () => {
    setLoading(true);
    try {
      const data = await getLibros();
      setLibros(data);
    } finally {
      setLoading(false);
    }
  };

  const fetchPrestamos = async () => {
    const data = await getPrestamos();
    console.log("Prestamos desde backend:", data);
    setPrestamos(data);
  };

  useEffect(() => {
    fetchLibros();
    fetchPrestamos();
  }, []);

  const handlePrestar = async (libro) => {
    const ahora = new Date().toISOString();
    const espera = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString();

    const payload = {
      usuario_id: "692a0170c21678c65836349c", 
      libro_id: libro._id,
      fecha_prestamo: ahora,
      fecha_devolucion_esperada: espera
    };

    try {
      await crearPrestamo(payload);
      await fetchLibros();
      await fetchPrestamos(); 
      
      toast.success("📚 Libro prestado correctamente"); 
    } catch (e) {
      toast.error(e?.response?.data?.detail || "❌ Error al crear préstamo"); 
    }
  };

  const handleDevolver = async (prestamoId) => {
    try {
      const res = await devolverPrestamo(prestamoId);
        
      await fetchLibros();
      await fetchPrestamos(); 

      toast.success(`✅ Libro devuelto | Retraso: ${res.retraso_dias} días`); 
    } catch (e) {
      toast.error("❌ Error al devolver el libro"); 
    }
  };

  return (
    <div>
      <h2 className="text-xl mb-4">Libros</h2>
      {loading ? (
        <div>Cargando…</div>
      ) : (
        <BookList libros={libros} onPrestar={handlePrestar} onDevolver={handleDevolver} />
      )}

      <h2 className="text-xl mt-8 mb-4">Préstamos Activos</h2>
      <PrestamoList prestamos={prestamos} onDevolver={handleDevolver} />
    </div>
  );
}
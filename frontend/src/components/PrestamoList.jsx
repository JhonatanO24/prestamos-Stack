import React from "react";
import { motion } from "framer-motion";

export default function PrestamoList({ prestamos, onDevolver }) {
  return (
    <div className="mt-10">
      <div className="space-y-4">
        {prestamos.map((p) => (
          <motion.div
          key={p._id}
          whileHover={{ scale: 1.01 }}
          className="p-4 rounded-xl shadow-card" 
          style={{
            backgroundImage: "linear-gradient(to bottom right, #0f1724, #0b1220)",
            }}
            >
            <div className="flex justify-between items-center">
              <div>
                <p className="font-semibold">{p.libro.titulo}</p>
                <p className="text-sm text-gray-300">
                  Usuario: {p.usuario.nombre}
                </p>
                <p className="text-xs text-gray-400">
                  Devolver antes de: {new Date(p.fecha_devolucion_esperada).toLocaleDateString()}
                </p>
              </div>

              <button
                onClick={() => onDevolver(p._id)}
                className="btn bg-accent-500 hover:bg-accent-400"
              >
                Devolver
              </button>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
}

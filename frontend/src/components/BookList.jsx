import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import BookCard from "./BookCard";

export default function BookList({ libros = [], onPrestar, onDevolver }) {
  return (
    <AnimatePresence>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {libros.map((libro) => (
          <motion.div
            key={libro._id}
            layout
            initial={{ opacity: 0, y: 30, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, scale: 0.8 }}
            transition={{ duration: 0.25 }}
          >
            <BookCard
              libro={libro}
              onPrestar={() => onPrestar(libro)}
              onDevolver={() => {
                const prestamoId = libro.prestamo_id || libro._id;
                onDevolver(prestamoId);
              }}
            />
          </motion.div>
        ))}
      </div>
    </AnimatePresence>
  );
}

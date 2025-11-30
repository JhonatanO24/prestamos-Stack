import React from "react";
import { motion } from "framer-motion";

export default function BookCard({ libro, onPrestar, onDevolver }) {
    if (!libro) {
        return null;
    }

    const disponible = libro.disponible !== false;

    const statusClasses = disponible 
        ? 'bg-emerald-600/20 text-emerald-300 border border-emerald-500/30' 
        : 'bg-red-600/20 text-red-300 border border-red-500/30';

    return (
        <motion.div
            whileHover={{ y: -4, scale: 1.01, boxShadow: "0px 6px 30px rgba(139,92,246,0.45)" }}
            className="p-5 rounded-xl shadow-lg transition-shadow duration-300 flex flex-col justify-between"
            style={{
                backgroundImage: "linear-gradient(to bottom right, #1f2937, #111827)", 
            }}
        >
            <div className="flex items-start justify-between mb-4">
                <div>
                    <h3 className="text-xl font-bold text-white mb-1 leading-tight">{libro.titulo}</h3>
                    <p className="text-sm text-gray-400">{libro.autor}</p>
                </div>

                <div className="text-sm">
                    <span 
                        className={`px-3 py-1 rounded-full text-xs font-semibold transition-colors ${statusClasses}`}
                    >
                        {disponible ? 'Disponible' : 'Prestado'}
                    </span>
                </div>
            </div>

            <div className="mt-4 flex justify-end">
                {disponible && ( 
                    <motion.button
                        whileTap={{ scale: 0.95 }}
                        onClick={() => onPrestar(libro)}
                        className="px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors duration-200 shadow-md"
                    >
                        Prestar
                    </motion.button>
                )}
            </div>
        </motion.div>
    );
}
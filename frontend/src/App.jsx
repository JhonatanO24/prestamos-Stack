import React from "react";
import Home from "./pages/Home"; 

export default function App() {
  return (
    
    <div className="min-h-screen p-6">
      <header className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold text-primary-300">Préstamos · Biblioteca</h1>
        <div className="text-sm text-muted-foreground">Demo • FastAPI + MongoDB</div>
      </header>

      <main>
        <Home />
      </main>
    </div> 
  );
}


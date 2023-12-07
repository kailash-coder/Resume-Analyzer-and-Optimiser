import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import { Home, Analysis } from "./pages";

const App = () => {
  return (
    <BrowserRouter>
      <div className="w-full bg-[#0E0021] min-h-[100vh]">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/analysis" element={<Analysis />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;

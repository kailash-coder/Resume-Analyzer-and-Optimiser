// eslint-disable-next-line no-unused-vars
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { logo, backimg } from "../assets";

const Home = () => {
  const navigate = useNavigate();

  const handleTryIt = () => {
    navigate("/analysis");
  };

  return (
    <>
      <div className="w-full flex flex-row justify-center items-center">
        <div className="w-2/5 h-screen bg-[0E0021] flex flex-col justify-between items-center">
          <header className="w-full flex justify-between items-center  sm:px-8 px-4 py-4">
            <a href="/">
              <img src={logo} alt="logo" className="w-[110px]" />
            </a>
          </header>
          <div className="flex flex-col mb-24 justify-center items-center">
            <h1 className="text-3xl text-white">Get Started</h1>
            <button
              onClick={handleTryIt}
              className="px-3 py-3 w-24 text-white text-sm font-normal bg-[#560043] border-[1.5px] border-[#eee] border-solid rounded-2xl mt-5"
            >
              Try it
            </button>
          </div>
          <div className="text-xs text-white mb-2">
            <p>Privacy Policy | Terms & Conditions</p>
          </div>
        </div>

        <div className="w-3/5 h-screen bg-black relative">
          <div
            /* className="w-full h-screen relative" */
            className="absolute inset-0 bg-cover bg-center"
            style={{ backgroundImage: `url(${backimg})`, opacity: 0.08 }}
          ></div>
          <div className="relative z-10 p-8"></div>
        </div>
      </div>
    </>
  );
};

export default Home;

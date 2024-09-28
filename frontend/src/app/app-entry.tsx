import { createRoot } from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import { createRouter } from "./providers/app-router";
import "@/shared/styles/globals.css";
const root = document.getElementById("root")! as HTMLElement;

createRoot(root).render(<RouterProvider router={createRouter()} />);

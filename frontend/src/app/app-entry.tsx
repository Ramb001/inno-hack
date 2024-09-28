import { createRoot } from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import { createRouter } from "./providers/app-router";
import "@/shared/styles/globals.css";
import { Provider } from "react-redux";
import { appStore } from "./providers/app-store";
const root = document.getElementById("root")! as HTMLElement;

createRoot(root).render(
  <Provider store={appStore}>
    <RouterProvider router={createRouter()} />
  </Provider>
);

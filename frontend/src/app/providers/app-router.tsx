import { MainPage } from "@/pages/main";
import { createBrowserRouter } from "react-router-dom";
import { Layout } from "../layout/layout";

export const createRouter = () =>
  createBrowserRouter([
    {
      element: <Layout />,
      children: [
        {
          path: "/",
          element: <MainPage />,
        },
      ],
    },
  ]);

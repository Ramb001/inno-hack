import { MainPage } from "@/pages/main";
import { createBrowserRouter, Navigate } from "react-router-dom";
import { Layout } from "../layout/layout";
import { LoginPage } from "@/pages/login";

export const createRouter = () =>
  createBrowserRouter([
    {
      path: "/",
      element: <Navigate to="/login" />,
    },
    {
      path: "/login",
      element: <LoginPage />,
    },
    {
      element: <Layout />,
      children: [
        {
          path: "/main",
          element: <MainPage />,
        },
      ],
    },
  ]);

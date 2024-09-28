import { Header } from "@/widgets/header";
import { Sidebar } from "@/widgets/sidebar";
import { Outlet } from "react-router-dom";

export const Layout = () => {
  return (
    <div className="min-h-screen  flex">
      <Sidebar />
      <div className="w-full">
        <Header />
        <main className="p-4 flex-grow ">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { Avatar, AvatarImage, AvatarFallback } from "@/shared/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/shared/ui/dropdown-menu";

import { LogOut } from "lucide-react";

export const Profile = () => {
  const [userData] = useState(JSON.parse(String(sessionStorage.getItem("userData"))));

  const navigate = useNavigate();

  function logout() {
    sessionStorage.removeItem("userData");
    navigate("/");
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Avatar className="">
          <AvatarImage src="" alt="@avatar" />
          <AvatarFallback className="duration-200 hover:bg-gray-200">
            {userData?.name?.slice(0, 1) ?? "PR"}
          </AvatarFallback>
        </Avatar>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-56">
        <DropdownMenuLabel>{userData?.name ?? "Имя аккаунта"}</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuItem>Профиль</DropdownMenuItem>
        <DropdownMenuItem>GitHub</DropdownMenuItem>
        <DropdownMenuSeparator />
        <DropdownMenuItem onClick={logout} className="flex-row-reverse justify-between">
          <LogOut size={18} color="#9e0000" />
          Выйти
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
};

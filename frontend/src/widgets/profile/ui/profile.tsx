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
  const userName = sessionStorage.getItem("username");

  console.log(userName);

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Avatar className="">
          <AvatarImage src="" alt="@avatar" />
          <AvatarFallback className="duration-200 hover:bg-gray-200">
            {userName?.slice(0, 1) ?? "PR"}
          </AvatarFallback>
        </Avatar>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-56">
        <DropdownMenuLabel>{userName ?? "Имя аккаунта"}</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuItem>Профиль</DropdownMenuItem>
        <DropdownMenuItem>GitHub</DropdownMenuItem>
        <DropdownMenuSeparator />
        <DropdownMenuItem className="flex-row-reverse justify-between">
          <LogOut size={18} color="#9e0000" />
          Выйти
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
};

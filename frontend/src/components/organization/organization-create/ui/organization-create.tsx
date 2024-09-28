import { useState } from "react";
import { Button } from "@/shared/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/shared/ui/dialog";
import { PlusSquare } from "lucide-react";
import { Input } from "@/shared/ui/input";

export const OrganizationCreate = () => {
  const [organizationName, setOrganizationName] = useState("");

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setOrganizationName(e.target.value);
  };

  const handleSubmit = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    // Здесь добавьте логику для создания организации
    console.log("Создать организацию:", organizationName);
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button className="p-1 bg-transparent hover:bg-gray-200 transition duration-200">
          <PlusSquare color="black" />
        </Button>
      </DialogTrigger>
      <DialogContent className="min-h-[300px] min-w-[500px] grid grid-cols-1 grid-rows-2 items-start">
        <DialogHeader>
          <DialogTitle>Создать организацию</DialogTitle>
          <DialogDescription>
            Пожалуйста, введите название вашей организации.
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={() => handleSubmit} className="flex flex-col gap-4">
          <label htmlFor="organization-name" className="flex flex-col">
            <span className="text-gray-700">Название организации</span>
            <Input
              id="organization-name"
              type="text"
              value={organizationName}
              onChange={handleInputChange}
              placeholder="Введите название"
              className="border border-gray-200 rounded-lg p-2 focus:outline-none focus:ring-2 transition duration-200"
              required
            />
          </label>
          <Button
            type="submit"
            className="bg-gray-700 text-white transition duration-200"
          >
            Создать
          </Button>
        </form>
      </DialogContent>
    </Dialog>
  );
};

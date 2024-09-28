export type Task = {
  id: number;
  status: string | "Completed" | "Low" | "High";
  title: string;
  content: string;
  members: string[];
  columnId: number;
};

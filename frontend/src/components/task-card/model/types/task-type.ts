export type Task = {
  status: string | "Completed" | "Low" | "High";
  title: string;
  content: string;
  members: string[];
};

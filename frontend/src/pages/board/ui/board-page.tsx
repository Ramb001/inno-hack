import { KanbanBoard } from "@/components/task-table";
import { useParams } from "react-router-dom";

export const BoardPage = () => {
  const { boardId } = useParams();
  console.log(boardId?.slice(1, boardId.length));
  const currencyBoardId = Number(boardId?.slice(1, boardId.length));

  return <KanbanBoard organizationId={currencyBoardId} />;
};

'use client';

import React, { useState, useEffect } from "react";
import {
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
  Tooltip,
  Chip,
  Pagination,
  Spinner,
} from "@nextui-org/react";
import { FaEye, FaEdit, FaTrash } from "react-icons/fa";
import {DefaultService} from "@client";


export default function DatalakeTable() {
  const [datalakes, setDatalakes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedDatalakeName, setSelectedDatalakeName] = useState(null);
  const [selectedDatalakeData, setSelectedDatalakeData] = useState([]);
  const [dataLoading, setDataLoading] = useState(false);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [knrQuery, setKnrQuery] = useState(null);

  useEffect(() => {
    const fetchDatalakes = async () => {
      setLoading(true);
      try {

		const response: any = await DefaultService.getListApiDatalakeGet();

		const datalakeObjects = response.tables.map((name, index) => ({
			id: index,
			name: name,
		  }));
        setDatalakes(datalakeObjects);
      } catch (error) {
        console.error("Error fetching datalakes:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchDatalakes();
  }, []);

  const handleViewDatalake = async (datalakeName) => {
    setSelectedDatalakeName(datalakeName);
    setPage(1);
    await fetchDatalakeData(datalakeName, 1);
  };

  const fetchDatalakeData = async (datalakeName, pageNumber) => {
    setDataLoading(true);
    try {
	  const response: any = await DefaultService.getTableApiDatalakeTableNameGet({
		tableName: datalakeName,
		page: pageNumber,
		perPage: 5,
		knrQuery: knrQuery,
	  });
      setSelectedDatalakeData(response.data);
      const totalCount = response.total_count;
      setTotalPages(Math.ceil(totalCount / 10));
    } catch (error) {
      console.error("Error fetching datalake data:", error);
    } finally {
      setDataLoading(false);
    }
  };

  const handleDataPageChange = (newPage) => {
    setPage(newPage);
    fetchDatalakeData(selectedDatalakeName, newPage);
  };

  const renderCell = (datalake, columnKey) => {
    switch (columnKey) {
      case "name":
        return <Chip>{datalake.name}</Chip>;
      case "actions":
        return (
          <div className="relative flex items-center gap-2">
            <Tooltip content="Visualizar">
              <span
                className="text-lg text-default-400 cursor-pointer active:opacity-50"
                onClick={() => handleViewDatalake(datalake.name)}
              >
                <FaEye />
              </span>
            </Tooltip>
            <Tooltip content="Editar">
              <span className="text-lg text-default-400 cursor-pointer active:opacity-50">
                <FaEdit />
              </span>
            </Tooltip>
            <Tooltip color="danger" content="Excluir">
              <span className="text-lg text-danger cursor-pointer active:opacity-50">
                <FaTrash />
              </span>
            </Tooltip>
          </div>
        );
      default:
        return datalake[columnKey] || "N/A";
    }
  };

  const columns = [
    { name: "Datalake", uid: "name" },
    { name: "Ações", uid: "actions" },
  ];

  return (
    <>
      {loading ? (
        <div className="flex justify-center items-center h-64">
          <Spinner size="lg" />
        </div>
      ) : (
        <Table
          aria-label="Datalake Table"
          style={{ height: "auto", minWidth: "100%" }}
        >
          <TableHeader columns={columns}>
            {(column) => (
              <TableColumn
                key={column.uid}
                align={column.uid === "actions" ? "center" : "start"}
              >
                {column.name}
              </TableColumn>
            )}
          </TableHeader>
          <TableBody items={datalakes || []}>
            {(item) => (
              <TableRow key={item.id}>
                {(columnKey) => (
                  <TableCell>{renderCell(item, columnKey)}</TableCell>
                )}
              </TableRow>
            )}
          </TableBody>
        </Table>
      )}

      {selectedDatalakeName && (
        <div className="mt-10 w-full flex flex-col items-center">
          <h3>Datalake selecionado: <b>{selectedDatalakeName}</b></h3>
          <div className="mb-4">
            <input
              type="text"
              placeholder="Procurar KNR"
              value={knrQuery || ''}
              onChange={(e) => setKnrQuery(e.target.value || null)}
              className="border rounded px-3 py-2"
            />
            <button
              onClick={() => fetchDatalakeData(selectedDatalakeName, 1)}
              className="ml-2 px-4 py-2 bg-blue-500 text-white rounded"
            >
              Buscar
            </button>
          </div>
          {dataLoading ? (
            <div className="flex justify-center items-center h-64">
              <Spinner size="lg" />
            </div>
          ) : (
            <>
              <Table
                aria-label="Datalake Data Table"
                style={{ height: "auto", minWidth: "100%" }}
              >
                <TableHeader>
                  {selectedDatalakeData.length > 0 &&
                    Object.keys(selectedDatalakeData[0] || {}).map((key) => (
                      <TableColumn key={key}>{key}</TableColumn>
                    ))}
                </TableHeader>
                <TableBody items={selectedDatalakeData || []}>
                  {(item) => (
                    <TableRow key={item.id || item.index || Math.random()}>
                      {(columnKey) => (
                        <TableCell>{item[columnKey] || "N/A"}</TableCell>
                      )}
                    </TableRow>
                  )}
                </TableBody>
              </Table>
              <div className="flex justify-center mt-4">
                <Pagination
                  total={totalPages}
                  initialPage={page}
                  onChange={handleDataPageChange}
                />
              </div>
            </>
          )}
        </div>
      )}
    </>
  );
}

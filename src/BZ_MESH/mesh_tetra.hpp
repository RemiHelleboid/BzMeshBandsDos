/**
 * @file mesh_tetra.hpp
 * @author Rémi Helleboid (remi.helleboid@st.com)
 * @brief
 * @version 0.1
 * @date 2022-07-14
 *
 * @copyright Copyright (c) 2022
 *
 */
#pragma once

#include <array>
#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <functional>

#include "mesh_vertex.hpp"

namespace bz_mesh {

class Tetra {
 private:
    /**
     * @brief Element index.
     *
     */
    std::size_t m_index;

    /**
     * @brief The 4 vertices of the tetrahedra are stored as an array of pointers on Vertices object.
     *
     */
    std::array<Vertex*, 4> m_list_vertices{nullptr, nullptr, nullptr, nullptr};

    /**
     * @brief List of the edges vectors of the tetrahedra.
     * Stored as follows: [v01, v02, v03, v12, v13, v23]
     * where for example v13 = m_list_vertices[1] - m_list_vertices[3].
     *
     */
    std::array<vector3, 6> m_list_edges{};

    /**
     * @brief Signed volume of the tetrahedra.
     * The sign depends on the "orientation" of the tetrahedra.
     *
     */
    double m_signed_volume;

    /**
     * @brief Number of conduction bands.
     *
     */
    std::size_t m_nb_bands = 0;

 public:
    static std::vector<double> ms_case_stats;

    /**
     * @brief There is not default constructor for Tetra class.
     *
     */
    Tetra() = delete;

    Tetra(std::size_t index, const std::array<Vertex*, 4>& list_vertices);

    std::vector<double> get_band_energies_at_vertices(std::size_t index_band) const;

    double                compute_signed_volume() const;
    double                get_signed_volume() const { return m_signed_volume; }
    vector3               compute_edge(std::size_t index_vtx_1, std::size_t index_vtx_2) const;
    bool                  is_location_inside(const vector3& location) const;
    std::array<double, 4> compute_barycentric_coordinates(const vector3& location) const;
    vector3               compute_euclidean_coordinates(const std::array<double, 4>& barycentric_coordinates) const;
    vector3               compute_euclidean_coordinates_with_indices(const std::array<double, 4>& barycentric_coordinates,
                                                                     const std::array<int, 4>&    indices_vertex) const;

    std::array<int, 4>   get_index_vertices_with_sorted_energy_at_band(std::size_t index_band) const;
    std::vector<vector3> compute_band_iso_energy_surface(double iso_energy, std::size_t band_index) const;
    double               compute_tetra_dos_band(double energy, std::size_t band_index) const;

    static void reset_stat_iso_computing() { ms_case_stats = std::vector<double>(5, 0.0); }

    static void print_stat_iso_computing() {
        std::size_t total_computation = ms_case_stats[0] + ms_case_stats[1] + ms_case_stats[2] + ms_case_stats[3] + ms_case_stats[4];
        std::cout << "Case 1:       " << ms_case_stats[0] / double(total_computation) << std::endl;
        std::cout << "Case 2:       " << ms_case_stats[1] / double(total_computation) << std::endl;
        std::cout << "Case 3:       " << ms_case_stats[2] / double(total_computation) << std::endl;
        std::cout << "Case 4:       " << ms_case_stats[3] / double(total_computation) << std::endl;
        std::cout << "Case 5:       " << ms_case_stats[4] / double(total_computation) << std::endl;
        std::cout << "Case Unknown: " << 1 - std::accumulate(ms_case_stats.begin(), ms_case_stats.end(), 0.0) / double(total_computation)
                  << std::endl;
    }
};

}  // namespace bz_mesh